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

# Function: handle_missing_values
# Purpose: Fill or drop missing values based on column type
# Why: Ensures data integrity for analysis
def handle_missing_values(df):
    """
    Fill missing values: categorical columns get 'Unknown', numeric columns get the median.
    """
    df = df.copy()  # Avoid modifying the original DataFrame

    # Fill missing values in categorical columns with 'Unknown'
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna('Unknown')

    # Fill missing values in numeric columns with the median
    for col in df.select_dtypes(include=['number']).columns:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)

    return df


# Function: remove_invalid_rows
# Purpose: Remove rows with negative sales or quantities
# Why: Negative values are not valid in this context
def remove_invalid_rows(df):
    """
    Remove rows where 'sales_amount' or 'quantity_sold' are negative.
    """
    df = df.copy()  # Avoid modifying the original DataFrame

    # Keep only rows where sales_amount and quantity_sold are non-negative
    df = df[(df['sales_amount'] >= 0) & (df['quantity_sold'] >= 0)]

    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())