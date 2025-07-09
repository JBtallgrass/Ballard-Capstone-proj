# utils.py

import logging
import re
from collections import Counter
import pandas as pd
import numpy as np

# --- Function: Standardize Column Names ---
def standardize_column_names(df):
    """
    Standardizes DataFrame column names: lowercase, underscores, and alphanumeric only.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[ \-]+", "_", regex=True)
        .str.replace(r"[^\w_]", "", regex=True)
    )
    return df
# --- Function: Extract and Standardize Key Indicator Columns ---
def extract_key_indicators(df, min_year=2020):
    """
    Extracts and assigns key socioeconomic indicators from a DataFrame based on the most common year in column names.

    Args:
        df (pd.DataFrame): The dataset to process.
        min_year (int): Minimum year to consider when extracting indicators.

    Returns:
        tuple: (updated DataFrame, dictionary of used columns, year extracted)
    """
    year = extract_common_year_from_columns(df, min_year=min_year)
    logging.info(f"📅 Most common year in column names: {year}")

    # Column matching logic
    education_cols = [col for col in df.columns if ('bachelor' in col or 'high_school' in col) and str(year) in col]
    poverty_cols = [col for col in df.columns if 'poverty' in col and str(year) in col]
    unemployment_cols = [col for col in df.columns if 'unemployment' in col and str(year) in col]
    population_cols = [col for col in df.columns if ('population' in col or 'census' in col) and str(year) in col]

    # Log discovered matches
    logging.info(f"📚 Education columns: {education_cols}")
    logging.info(f"📉 Poverty columns: {poverty_cols}")
    logging.info(f"💼 Unemployment columns: {unemployment_cols}")
    logging.info(f"👥 Population columns: {population_cols}")

    # Assign standardized columns (or NaN fallback)
    df['BachelorsDegreeRate'] = df.get(education_cols[0], np.nan) if education_cols else np.nan
    df['HighSchoolGradRate'] = df.get(education_cols[1], np.nan) if len(education_cols) > 1 else np.nan
    df['PovertyRate'] = df.get(poverty_cols[0], np.nan) if poverty_cols else np.nan
    df['UnemploymentRate'] = df.get(unemployment_cols[0], np.nan) if unemployment_cols else np.nan
    df['Population'] = df.get(population_cols[0], np.nan) if population_cols else np.nan
    df['Year'] = year

    used = {
        'education': education_cols,
        'poverty': poverty_cols,
        'unemployment': unemployment_cols,
        'population': population_cols
    }

    return df, used, year

# --- Function: Filter to County-Level Rows ---
def filter_to_county_level(df):
    """
    Removes state-level and summary rows based on FIPS and county name content.
    """
    for fips_col in ['fips', 'fips_code', 'fipstxt']:
        if fips_col in df.columns:
            df = df[df[fips_col].astype(str).str[-3:] != '000']
    if 'county' in df.columns:
        df = df[~df['county'].str.contains("state|total|arkansas", case=False, na=False)]
    return df

# --- Function: Log Duplicate County-Attribute Pairs ---
def log_duplicate_attributes(df, key="unknown"):
    """
    Logs a warning if duplicate (county, attribute) pairs are found.
    """
    if df.duplicated(subset=['county', 'attribute']).any():
        logging.warning(f"⚠️ {key} has duplicate county-attribute pairs.")

# --- Function: Extract Most Common Year from Column Names ---
def extract_common_year_from_columns(df, return_all=False, min_freq=1, min_year=2020):
    """
    Extracts the most common 4-digit year from column names based on a minimum year.
    
    Args:
        df (pd.DataFrame): DataFrame with columns to check.
        return_all (bool): If True, returns all years and their counts.
        min_freq (int): Minimum frequency required to include a year (if return_all=True).
        min_year (int): Only consider years >= this value.

    Returns:
        str or dict: Most frequent year (as string) or dict of {year: count}
    """
    year_pattern = re.compile(r'\b(?:19|20)\d{2}\b')  # non-capturing group
    years = []

    for col in df.columns:
        matches = year_pattern.findall(col)
        years.extend(matches)

    # Filter to years >= min_year
    filtered_years = [y for y in years if y.isdigit() and int(y) >= min_year]

    year_counts = Counter(filtered_years)

    if return_all:
        return {year: count for year, count in year_counts.items() if count >= min_freq}
    elif year_counts:
        return year_counts.most_common(1)[0][0]
    else:
        return None

# --- Function: Subset Columns to Given Year ---
def subset_columns_by_year(df, year):
    """
    Returns a DataFrame with only the columns that contain the specified year.
    """
    return df[[col for col in df.columns if str(year) in col]].copy()

# --- Constant: North Central Arkansas Counties ---
nca_counties = [
    'baxter', 'cleburne', 'fulton', 'independence', 'izard', 'jackson',
    'marion', 'searcy', 'sharp', 'stone', 'van buren', 'white', 'woodruff'
]

# --- Confirmation Log ---
logging.info("✅ Utility functions loaded from utils.py")
