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
            ["Preview", "Overview", "Data Types", "Missing Values", "Correlation Matrix and Heatmap", "Pairplot", "Distribution Plots"]
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
    else:
        st.sidebar.write("Please upload a CSV file.")

if __name__ == "__main__":
    main()
