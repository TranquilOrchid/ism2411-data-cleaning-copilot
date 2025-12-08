# This script loads the raw sales dataset, applies cleaning steps, and saves a cleaned version.
# Steps include: standardizing column names, trimming whitespace, handling missing values, and removing invalid (negative) data.

import pandas as pd

# Function: load_data
# Purpose: Load the raw CSV file into a DataFrame.
# Why: Allows us to reuse this function and keep code organized.
def load_data(file_path):
    """
    Reads a CSV file into a pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

# Function: clean_column_names
# Purpose: Standardize column names for consistency
# Why: Easier to reference columns in later cleaning steps
def clean_column_names(df):
    df = df.copy()  # Avoid changing original DataFrame directly
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df