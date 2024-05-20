import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# Custom CSS for buttons and sidebar
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        padding-top: 20px;
        background-color: #000000; /* Black background */
    }
    .sidebar .sidebar-content h1, h2, h3, h4, h5, h6 {
        color: white; /* White text for headings */
    }
    .btn {
        display: block;
        width: 100%;
        padding: 10px;
        margin: 5px 0;
        text-align: center;
        border-radius: 5px;
        color: white;
        background-color: #000000;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .btn:hover {
        background-color: #0056b3;
    }
    .btn.active {
        background-color: #004085;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Function to load data
def load_data(file_path):
    try:
        return pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(file_path, encoding='ISO-8859-1')

# Function to display data preview
def display_data_preview(data):
    st.write("## Data Preview")
    st.dataframe(data.head(20))

# Function to display basic statistics
def display_basic_statistics(data):
    st.write("## Basic Statistics")
    st.write(data.describe())

# Function to display data types
def display_data_types(data):
    st.write("## Data Types")
    st.write(data.dtypes)

# Function to display missing values
def display_missing_values(data):
    st.write("## Missing Values")
    st.write(data.isnull().sum())

# Function to display correlation matrix and heatmap
def display_correlation_matrix(data):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    st.write("## Correlation Matrix")
    if not numeric_data.empty:
        corr = numeric_data.corr()
        st.write(corr)
        
        st.write("## Correlation Heatmap")
        fig = ff.create_annotated_heatmap(
            z=corr.values,
            x=list(corr.columns),
            y=list(corr.index),
            annotation_text=corr.round(2).values,
            colorscale='Viridis'
        )
        st.plotly_chart(fig)
    else:
        st.write("No numeric data available for correlation matrix.")

# Function to display pairplot
def display_pairplot(data):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    st.write("## Pairplot")
    if not numeric_data.empty:
        fig = px.scatter_matrix(numeric_data, height=800, width=800)
        st.plotly_chart(fig)
    else:
        st.write("No numeric data available for pairplot.")

# Function to display distribution plots
def display_distribution_plots(data):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    st.write("## Distribution Plots")
    for column in numeric_data.columns:
        st.write(f"### Distribution of {column}")
        fig = px.histogram(data, x=column, nbins=30, marginal="box", title=f"Distribution of {column}", height=400, width=600)
        st.plotly_chart(fig)

# Function to clean data
def clean_data(data):
    st.write("## Data Cleaning")
    
    if st.checkbox("Drop missing values"):
        data = data.dropna()
    
    if st.checkbox("Drop duplicates"):
        data = data.drop_duplicates()

    return data

# Function to filter data
def filter_data(data):
    st.write("## Custom Queries")
    column = st.selectbox("Select Column", data.columns)
    st.write(f"Data Type: {data[column].dtype}")
    condition = st.text_input("Enter Condition (e.g., > 50)")
    if st.button("Apply Filter"):
        try:
            filtered_data = data.query(f"{column} {condition}")
            st.write(f"Filtered Data (Rows: {filtered_data.shape[0]})")
            st.dataframe(filtered_data)
        except Exception as e:
            st.error(f"Error: {e}")

# Function to generate summary report
def generate_summary_report(data):
    st.write("## Summary Report")
    st.write(data.describe())
    st.write("Missing Values")
    st.write(data.isnull().sum())
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    if not numeric_data.empty:
        st.write("Correlation Matrix")
        st.write(numeric_data.corr())

# Function to display welcome message and image
def display_welcome():
    st.image(r"C:\Users\LENOVO\OneDrive - Texas State University\Desktop\dashboard\prompthero-prompt-ff9bdc63ada.png", use_column_width=True)
    st.write("### Welcome to CSV Analyzer!")
    st.write("Upload your CSV file to get started and explore various data analysis features.")

# Main function to display the app
def main():
    # Initialize session state
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    st.sidebar.title("CSV File Analyzer")
    st.sidebar.write("Upload a CSV file to perform EDA")
    
    # Upload CSV file
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    # Navigation buttons in the sidebar
    st.sidebar.title("Navigation")

    with st.sidebar.expander("Data Overview"):
        if st.sidebar.button("Home", key="Home"):
            st.session_state.page = "Home"
        if st.sidebar.button("Preview", key="Preview"):
            st.session_state.page = "Preview"
        if st.sidebar.button("Overview", key="Overview"):
            st.session_state.page = "Overview"
    
    with st.sidebar.expander("Data Insights"):
        if st.sidebar.button("Data Types", key="Data Types"):
            st.session_state.page = "Data Types"
        if st.sidebar.button("Missing Values", key="Missing Values"):
            st.session_state.page = "Missing Values"
        if st.sidebar.button("Correlation Matrix and Heatmap", key="Correlation Matrix and Heatmap"):
            st.session_state.page = "Correlation Matrix and Heatmap"
        if st.sidebar.button("Pairplot", key="Pairplot"):
            st.session_state.page = "Pairplot"
        if st.sidebar.button("Distribution Plots", key="Distribution Plots"):
            st.session_state.page = "Distribution Plots"
    
    with st.sidebar.expander("Data Management"):
        if st.sidebar.button("Data Cleaning", key="Data Cleaning"):
            st.session_state.page = "Data Cleaning"
        if st.sidebar.button("Custom Queries", key="Custom Queries"):
            st.session_state.page = "Custom Queries"
        if st.sidebar.button("Summary Report", key="Summary Report"):
            st.session_state.page = "Summary Report"

    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.experimental_set_query_params(page="Home")
        if st.session_state.page == "Preview":
            display_data_preview(data)
        elif st.session_state.page == "Overview":
            display_basic_statistics(data)
        elif st.session_state.page == "Data Types":
            display_data_types(data)
        elif st.session_state.page == "Missing Values":
            display_missing_values(data)
        elif st.session_state.page == "Correlation Matrix and Heatmap":
            display_correlation_matrix(data)
        elif st.session_state.page == "Pairplot":
            display_pairplot(data)
        elif st.session_state.page == "Distribution Plots":
            display_distribution_plots(data)
        elif st.session_state.page == "Data Cleaning":
            cleaned_data = clean_data(data)
            st.write("## Cleaned Data Preview")
            st.dataframe(cleaned_data.head(20))

            # Download cleaned data
            csv = cleaned_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download cleaned data as CSV",
                data=csv,
                file_name='cleaned_data.csv',
                mime='text/csv',
            )
        elif st.session_state.page == "Custom Queries":
            filter_data(data)
        elif st.session_state.page == "Summary Report":
            generate_summary_report(data)
        else:
            display_welcome()
    else:
        display_welcome()

if __name__ == "__main__":
    main()
