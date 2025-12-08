# This script loads the raw sales dataset, cleans it, and saves a cleaned version.
# Cleaning steps include: standardizing column names, normalizing text, fixing numeric columns,
# filling missing values, removing invalid rows, and deduplicating products.

import pandas as pd

# Load raw CSV
def load_data(file_path):
    """Reads a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

# Standardize column names
def clean_column_names(df):
    """Lowercase, replace spaces with underscores, and strip column names."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

# Normalize text columns
def normalize_text_columns(df, text_columns):
    """Strip quotes/spaces, remove extra internal spaces, and capitalize text."""
    df = df.copy()
    for col in text_columns:
        df[col] = df[col].astype(str)           # Ensure strings
        df[col] = df[col].str.replace('"', '')  # Remove quotes
        df[col] = df[col].str.strip()           # Remove leading/trailing spaces
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True)  # Remove extra internal spaces
        df[col] = df[col].str.title()           # Capitalize each word
    return df

# Fix numeric columns
def fix_numeric_columns(df, numeric_columns):
    """Convert to numeric, invalid parsing becomes NaN."""
    df = df.copy()
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

# Fill missing values
def handle_missing_values(df):
    """Fill categorical columns with 'Unknown', numeric columns with median."""
    df = df.copy()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna('Unknown')
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].median())
    return df

# Remove negative numeric values
def remove_invalid_rows(df):
    """Remove rows where any numeric column is negative."""
    df = df.copy()
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        df = df[df[col] >= 0]
    return df

# Deduplicate products
def deduplicate_products(df):
    """
    Combine duplicate products (same prodname & category) by taking median of numeric values.
    Keeps one row per unique product/category combination.
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include=['number']).columns
    df = df.groupby(['prodname', 'category'], as_index=False)[numeric_cols.tolist()].median()
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    # Load raw data
    df = load_data(raw_path)

    # Clean column names
    df = clean_column_names(df)

    # Normalize text columns
    df = normalize_text_columns(df, ['prodname', 'category'])

    # Fix numeric columns
    df = fix_numeric_columns(df, ['price', 'qty'])

    # Fill missing values
    df = handle_missing_values(df)

    # Remove negative numeric values
    df = remove_invalid_rows(df)

    # Deduplicate products
    df = deduplicate_products(df)

    # Preview cleaned data
    print("Columns after cleaning:", df.columns)
    print("First few rows after cleaning:")
    print(df.head())

    # Save cleaned CSV
    df.to_csv(cleaned_path, index=False)