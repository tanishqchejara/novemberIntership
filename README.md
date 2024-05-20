# Codes On Bytes: Data Science Internship Projects

This repository contains the code and documentation for the projects completed during the Data Science internship at Codes On Bytes from October to November 2023.

## Table of Contents

- [Introduction](#introduction)
- [Project 1: Create a CSV Dataset, Clean it, and Perform Data Preprocessing](#project-1-create-a-csv-dataset-clean-it-and-perform-data-preprocessing)
- [Project 2: Analyze the Dataset, Create Visualizations, and Train a Linear Regression Model](#project-2-analyze-the-dataset-create-visualizations-and-train-a-linear-regression-model)
- [Requirements](#requirements)
- [Usage](#usage)


## Introduction

This internship provided hands-on experience in the field of Data Science, covering various aspects of the data science workflow, including data acquisition, cleaning, preprocessing, exploratory analysis, visualization, and machine learning modeling.

## Project 1: Create a CSV Dataset, Clean it, and Perform Data Preprocessing

In this project, a CSV dataset was created either by extracting data from a public API or working with a predefined dataset. Subsequently, data cleaning and preprocessing techniques were applied to ensure data quality and reliability. The tasks included:

- Handling missing values
- Identifying and removing outliers
- Ensuring data consistency through data type conversions, duplicate removal, and categorical variable standardization
- Performing feature scaling and normalization

The cleaned and preprocessed dataset was then saved as a new CSV file for further analysis in Project 2.

**Code:** [`cleandataset.py`](cleandataset.py)

## Project 2: Analyze the Dataset, Create Visualizations, and Train a Linear Regression Model

Building upon the cleaned dataset from Project 1, this project focused on exploratory data analysis, data visualization, and machine learning model development. The main tasks included:

- Exploratory data analysis (EDA) using summary statistics, correlation analysis, and data distribution analysis
- Creating visualizations (scatter plots, line plots, bar charts, histograms, heatmaps) using libraries like Matplotlib and Seaborn
- Training and evaluating a linear regression model on the dataset
- Optimizing the model's performance through feature engineering, regularization, and hyperparameter tuning

**Code:** [`trainAndTest.py`](trainAndTest.py), [`visual.py`](visual.py)

## Requirements

The following Python libraries were used in these projects:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- requests

You can install the required libraries using pip:

## Usage

1. Clone the repository:
```bash 
git clone https://github.com/tanishqchejara/novemberIntership.git
```
2. Navigate to the project directory:
```bash
cd novemberIntership
```

3. Run the Python scripts for each project:
```bash
python cleandataset.py    # Project 1
python trainAndTest.py    # Project 2
python visual.py          # Project 2
```
