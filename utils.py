# utils.py

import logging
import re
from collections import Counter
import pandas as pd
import numpy as np


# --- Function: Standardize Column Names ---
def standardize_column_names(df):
    """
    Standardizes DataFrame column names to lowercase, underscores,
    and removes non-alphanumeric characters.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[ \-]+", "_", regex=True)
        .str.replace(r"[^\w_]", "", regex=True)
    )
    return df


# --- Function: Clean and Extract Year from 'attribute' column ---
def clean_and_extract_year(df):
    """
    Cleans 'attribute' column and extracts the most recent 4-digit year.

    Handles multi-year ranges like '2019–2023' or '2019–23'.

    Returns:
        DataFrame with cleaned 'attribute' column and new 'attribute_year' column.
    """
    df = df.copy()
    df['attribute'] = df['attribute'].str.strip().str.lower()
    df['attribute'] = df['attribute'].str.replace(r'__+', '_', regex=True).str.strip('_')

    def extract_year(attr):
        # Matches 2-digit or 4-digit years in multi-year ranges like '2019–23' or '2019-2023'
        matches = re.findall(r'(?:19|20)?\d{2}', attr)
        expanded = []
        for m in matches:
            if len(m) == 2:
                # Assume 2000s for 2-digit years unless context says otherwise
                expanded.append(f"20{m}")
            else:
                expanded.append(m)
        # Return the most recent year
        return max(expanded) if expanded else None

    df['attribute_year'] = df['attribute'].apply(extract_year)
    return df

# --- Function: Filter to County-Level Rows ---
def filter_to_county_level(df):
    """
    Removes state-level and summary rows using FIPS and county names.
    Preserves legitimate county names like 'Arkansas County'.
    """
    for fips_col in ['fips', 'fips_code', 'fipstxt']:
        if fips_col in df.columns:
            df = df[df[fips_col].astype(str).str[-3:] != '000']
    if 'county' in df.columns:
        df = df[~df['county'].str.contains(r'\b(state|total)\b', case=False, na=False)]
    return df


# --- Function: Log Duplicate County-Attribute Pairs ---
def log_duplicate_attributes(df, key="unknown"):
    """
    Logs a warning if duplicate (county, attribute) pairs are found.
    """
    if df.duplicated(subset=['county', 'attribute']).any():
        logging.warning(f"{key} has duplicate county-attribute pairs.")


# --- Function: Extract Most Common Year from Column Names ---
def extract_common_year_from_columns(df, return_all=False, min_freq=1, min_year=2020):
    """
    Finds the most common 4-digit year in column names.

    Returns:
        - most frequent year (as string), or
        - dict of year:count if return_all is True
    """
    year_pattern = re.compile(r'\b(?:19|20)\d{2}\b')
    years = []

    for col in df.columns:
        matches = year_pattern.findall(col)
        years.extend(matches)

    filtered_years = [y for y in years if y.isdigit() and int(y) >= min_year]
    year_counts = Counter(filtered_years)

    if return_all:
        return {year: count for year, count in year_counts.items() if count >= min_freq}
    elif year_counts:
        return year_counts.most_common(1)[0][0]
    else:
        return None


# --- Function: Subset Columns by Specific Year ---
def subset_columns_by_year(df, year):
    """
    Returns columns that contain a specific year string.
    """
    return df[[col for col in df.columns if str(year) in col]].copy()


# --- Function: Extract Key Socioeconomic Indicators ---
def extract_key_indicators(df, min_year=2022):
    """
    Identifies and standardizes key indicator columns:
    - BachelorsDegreeRate
    - HighSchoolGradRate
    - PovertyRate
    - UnemploymentRate
    - Population

    Now supports flexible matching and fallback logic.
    """
    year = extract_common_year_from_columns(df, min_year=min_year)
    logging.info(f"Most common year in column names: {year}")

    # Use regex-based matching to find flexible column names
    education_cols = [
        col for col in df.columns 
        if re.search(r"(bachelor|four.*college|high.*school|hs.*grad)", col, re.I)
    ]

    poverty_cols = [
        col for col in df.columns 
        if re.search(r"(poverty|povall|pctpov)", col, re.I) and str(year) in col
    ]

    unemployment_cols = [
        col for col in df.columns 
        if re.search(r"(unemployment.*rate|unemp_rate)", col, re.I) and str(year) in col
    ]

    population_cols = [
        col for col in df.columns 
        if re.search(r"(pop_estimate|population|census_2022_pop|estimates_base)", col, re.I) and str(year) in col
    ]

    # Log what was found
    # logging.info(f"Education columns: {education_cols}")
    logging.info(f"Poverty columns: {poverty_cols}")
    logging.info(f"Unemployment columns: {unemployment_cols}")
    logging.info(f"Population columns: {population_cols}")

    # Assign standardized variables with fallback logic
    df['BachelorsDegreeRate'] = df.get(education_cols[0], np.nan) if education_cols else np.nan
    df['HighSchoolGradRate'] = df.get(education_cols[1], np.nan) if len(education_cols) > 1 else np.nan
    df['PovertyRate'] = df.get(poverty_cols[0], np.nan) if poverty_cols else np.nan

    # Unemployment fallback if not matched
    if unemployment_cols:
        df['UnemploymentRate'] = df[unemployment_cols[0]]
    elif 'unemployment_rate_2022' in df.columns:
        df['UnemploymentRate'] = df['unemployment_rate_2022']
        logging.warning("Unemployment column not matched by regex. Using fallback 'unemployment_rate_2022'.")
    else:
        df['UnemploymentRate'] = np.nan

    df['Population'] = df.get(population_cols[0], np.nan) if population_cols else np.nan
    df['Year'] = year

    used = {
        'education': education_cols,
        'poverty': poverty_cols,
        'unemployment': unemployment_cols,
        'population': population_cols
    }

    return df, used, year

# --- Constant: North Central Arkansas Counties ---
nca_counties = [
    'baxter', 'cleburne', 'fulton', 'independence', 'izard', 'jackson',
    'marion', 'searcy', 'sharp', 'stone', 'van buren', 'white', 'woodruff'
]

# Updated export_to_latex_assets() with Recursive Search
def export_to_latex_assets(src_folder, dst_root="Capstone_Project_Report/images", generate_tex=False, delete_after=False):
    """
    Recursively copies .png and .csv files from `src_folder` and subdirectories to LaTeX-ready folders under `dst_root`,
    optionally generates .tex boilerplate, and deletes originals to save space.
    """
    # Ensure modules are available in function scope
    import os
    import shutil
    from pathlib import Path
    
    src_folder = Path(src_folder)
    dst_root = Path(dst_root)
    map_dir = dst_root / "maps"
    table_dir = dst_root / "tables"
    tex_dir = dst_root / "boilerplate"

    map_dir.mkdir(parents=True, exist_ok=True)
    table_dir.mkdir(parents=True, exist_ok=True)
    if generate_tex:
        tex_dir.mkdir(parents=True, exist_ok=True)

    # Recursively find all PNG and CSV files
    png_files = list(src_folder.rglob("*.png"))
    csv_files = list(src_folder.rglob("*.csv"))
    
    print(f"Found {len(png_files)} PNG files and {len(csv_files)} CSV files")
    
    # Process PNG files (maps/images)
    for src_path in png_files:
        filename = src_path.name
        dst_path = map_dir / filename
        
        # Handle duplicate filenames by adding parent directory name
        if dst_path.exists():
            parent_name = src_path.parent.name
            new_filename = f"{parent_name}_{filename}"
            dst_path = map_dir / new_filename
            filename = new_filename
        
        shutil.copy2(src_path, dst_path)
        print(f"Copied map: {filename} (from {src_path.relative_to(src_folder)})")
        
        if generate_tex:
            tex_code = (
                f"\\begin{{figure}}[!ht]\n"
                f"\\centering\n"
                f"\\includegraphics[width=0.85\\textwidth]{{images/maps/{filename}}}\n"
                f"\\caption{{Caption for {filename.replace('_', ' ').replace('.png','')}}}\n"
                f"\\label{{fig:{filename.replace('.png','').replace('_', '')}}}\n"
                f"\\end{{figure}}\n"
            )
            with open(tex_dir / f"{filename.replace('.png', '.tex')}", "w") as f:
                f.write(tex_code)

    # Process CSV files (tables)
    for src_path in csv_files:
        filename = src_path.name
        dst_path = table_dir / filename
        
        # Handle duplicate filenames by adding parent directory name
        if dst_path.exists():
            parent_name = src_path.parent.name
            new_filename = "{parent_name}_{filename}"
            dst_path = table_dir / new_filename
            filename = new_filename
        
        shutil.copy2(src_path, dst_path)
        print("Copied table: {filename} (from {src_path.relative_to(src_folder)})")
        
        if generate_tex:
            tex_comment = "% Table for {filename} located at images/tables/{filename}\n"
            with open(tex_dir / "{filename.replace('.csv', '.tex')}", "w") as f:
                f.write(tex_comment)

    # Delete originals if requested
    if delete_after:
        for src_path in png_files + csv_files:
            try:
                os.remove(src_path)
                print(f"Deleted original: {src_path.relative_to(src_folder)}")
            except Exception as e:
                print(f"Could not delete {src_path}: {e}")

    print("\n✅ All outputs transferred:")
    print("   📊 {len(png_files)} PNG files copied to: {map_dir}")
    print("   📋 {len(csv_files)} CSV files copied to: {table_dir}")
    if generate_tex:
        print("   📄 Boilerplate .tex files saved to: {tex_dir}")

    return {
        'png_files_copied': len(png_files),
        'csv_files_copied': len(csv_files),
        'destination': dst_root
    }

def load_arkansas_population_from_estimates(pop_file):
    """
    Load and return Arkansas county-level population data from a national Census CSV.

    Parameters:
        pop_file (Path or str): Path to the national PopulationEstimates.csv file

    Returns:
        DataFrame with ['GEOID', 'Population'] for Arkansas counties only
    """
    df = pd.read_csv(pop_file, encoding='cp1252', low_memory=False)
    df.columns = df.columns.str.strip()

    print("✅ Cleaned population file columns:", list(df.columns))
    print("🧪 Unique 'Attribute' values:", df['Attribute'].unique())

    # Try to select POP_ESTIMATE_2023, or fallback to any available estimate
    if 'POP_ESTIMATE_2023' in df['Attribute'].str.upper().unique():
        df = df[df['Attribute'].str.upper() == 'POP_ESTIMATE_2023'].copy()
    else:
        fallback_attr = df['Attribute'].iloc[0]
        print(f"⚠️ Falling back to first available attribute: {fallback_attr}")
        df = df[df['Attribute'] == fallback_attr].copy()

    # Rename and clean
    df = df.rename(columns={'FIPStxt': 'GEOID', 'Value': 'Population'})
    df['GEOID'] = df['GEOID'].astype(str).str.zfill(5)
    df['Population'] = pd.to_numeric(df['Population'], errors='coerce')

    # Keep Arkansas counties only (GEOID starts with '05')
    df = df[df['GEOID'].str.startswith('05')].copy()

    return df

# --- Confirmation Log ---
logging.info("Utility functions loaded from updated utils.py")
# --- End of utils.py ---