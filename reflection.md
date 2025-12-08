# Reflection on Data Cleaning Project

# What Copilot Generated

GitHub Copilot provided initial suggestions for functions like `load_data` and `clean_column_names`. I prompted it by writing descriptive comments above the function definitions, such as “Load the raw CSV file into a DataFrame” and “Standardize column names for consistency.” Copilot suggested the basic structure and some string manipulation methods, which gave me a good starting point.

# What I Modified

I made several important changes to Copilot’s code. For example, I added a new function, `normalize_text_columns`, to clean product names and categories by removing quotes, extra internal spaces, and standardizing capitalization. I also added `fix_numeric_columns` to handle invalid numeric values in `price` and `qty`. I modified `remove_invalid_rows` to remove negative values from any numeric column, not just specific ones. Finally, I added `deduplicate_products` to merge duplicate product entries using the median of numeric columns. These changes were necessary to handle the messy, inconsistent raw data effectively and produce a clean, usable CSV.

# What I Learned

I learned a lot about data cleaning in Python, especially using pandas. For example, I learned how to convert malformed numeric columns using `pd.to_numeric(errors='coerce')` and fill missing values with the median. I also learned the importance of normalizing text columns to handle inconsistent capitalization, quotes, and extra spaces. Regarding Copilot, I learned that it is a strong tool for generating boilerplate code quickly, but it often requires meaningful modifications to handle real-world data correctly. For instance, Copilot suggested cleaning column names, but I had to create additional functions to handle duplicates and malformed numeric values. This project reinforced the value of combining AI suggestions with careful, human-guided logic.

# Specific Example

One clear example was handling the raw sales data where multiple rows for the same product had inconsistent capitalization, extra spaces, and sometimes zero or negative quantities. Copilot did not handle these issues automatically, so I implemented functions to normalize text, convert numeric columns, remove negatives, and deduplicate products. This produced a clean, accurate dataset suitable for analysis and demonstration in a portfolio.