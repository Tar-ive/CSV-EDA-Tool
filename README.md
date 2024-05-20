# CSV File Analyzer

#You can check out the app here at :
(https://csvapp.streamlit.app/)

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Project Description
The **CSV File Analyzer** is a Streamlit-based application designed to provide users with an easy and interactive way to perform Exploratory Data Analysis (EDA) on CSV files. The primary goal of this project is to help users quickly understand the structure and characteristics of their data without needing extensive programming knowledge. This tool is particularly useful for data analysts, scientists, and anyone working with data who needs a quick, visual, and interactive way to explore their datasets.

## Features
- **Welcome Screen:** A fun and engaging welcome screen with an illustration and a brief introduction to the tool.
- **Data Preview:** View the first few rows of your dataset to get an initial understanding of its structure.
- **Basic Statistics:** Display basic statistical summaries of the numerical columns in your dataset.
- **Data Types:** List the data types of each column in your dataset.
- **Missing Values:** Identify missing values in your dataset and their counts.
- **Correlation Matrix and Heatmap:** Display a correlation matrix and an interactive heatmap for numerical columns.
- **Pairplot:** Create interactive pair plots to visualize relationships between numerical columns.
- **Distribution Plots:** Generate distribution plots for each numerical column.
- **Data Cleaning:** Options to drop missing values and duplicate rows.
- **Custom Queries:** Filter data based on custom conditions.
- **Summary Report:** Generate a summary report with key insights from the dataset.

## Installation
To run the CSV File Analyzer locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Tar-ive/Streamlit.git
    cd Streamlit
    ```

2. **Navigate to the main directory:**
    ```bash
    cd main
    ```

3. **Install the required libraries:**
    ```bash
    pip install streamlit pandas plotly
    ```

4. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Usage
1. **Launch the application:**
   After running the Streamlit command, the application will open in your default web browser.

2. **Upload a CSV file:**
   Use the file uploader on the sidebar to upload your CSV file.

3. **Navigate through the features:**
   Use the sidebar to navigate through various features such as Data Preview, Overview, Data Types, Missing Values, Correlation Matrix and Heatmap, Pairplot, Distribution Plots, Data Cleaning, Custom Queries, and Summary Report.

4. **Explore your data:**
   Interact with different features to explore and analyze your data visually and interactively.


### Data Preview
![Data Preview](images/data_preview.png)

### Correlation Heatmap
![Correlation Heatmap](images/correlation_heatmap.png)


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
