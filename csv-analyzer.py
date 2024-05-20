import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

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

# Main function to display the app
def main():
    st.sidebar.title("CSV File Analyzer")
    st.sidebar.write("Upload a CSV file to perform EDA")
    
    # Upload CSV file
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = load_data(uploaded_file)
        
        page = st.sidebar.selectbox(
            "Choose a page",
            ["Preview", "Overview", "Data Types", "Missing Values", "Correlation Matrix and Heatmap", "Pairplot", "Distribution Plots", "Data Cleaning", "Custom Queries", "Summary Report"]
        )

        if page == "Preview":
            display_data_preview(data)
        elif page == "Overview":
            display_basic_statistics(data)
        elif page == "Data Types":
            display_data_types(data)
        elif page == "Missing Values":
            display_missing_values(data)
        elif page == "Correlation Matrix and Heatmap":
            display_correlation_matrix(data)
        elif page == "Pairplot":
            display_pairplot(data)
        elif page == "Distribution Plots":
            display_distribution_plots(data)
        elif page == "Data Cleaning":
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
        elif page == "Custom Queries":
            filter_data(data)
        elif page == "Summary Report":
            generate_summary_report(data)
    else:
        st.image(r"prompthero-prompt-ff9bdc63ada.png", use_column_width=True)
        st.write("### Welcome to CSV Analyzer!")
        st.write("Upload your CSV file to get started and explore various data analysis features.")

if __name__ == "__main__":
    main()
