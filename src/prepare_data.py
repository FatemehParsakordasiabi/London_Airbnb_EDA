import argparse
from pathlib import Path
import pandas as pd
import numpy as np
from src.utils.io import read_csv, to_csv, ensure_dir

def clean_price(series: pd.Series) -> pd.Series:
    # Remove currency symbols and commas, then convert to float
    return (series.astype(str)
        .str.replace('[£$,]', '', regex=True)
        .str.replace(' ', '', regex=False)
        .replace({'': np.nan})
        .astype(float))

def booleanize(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().map({'t': 1, 'true': 1, 'y': 1, 'yes': 1, 'f': 0, 'false': 0, 'n': 0, 'no': 0}).fillna(0)

def parse_args():
    ap = argparse.ArgumentParser(description="Clean Airbnb listings data and generate processed CSV.")
    ap.add_argument('--input', type=str, default='data/raw/listings.csv', help='Path to raw listings.csv')
    ap.add_argument('--output', type=str, default='data/processed/listings_clean.csv', help='Path to save cleaned CSV')
    return ap.parse_args()

def main():
    args = parse_args()
    df = read_csv(args.input)

    # Standardize column names (snake_case)
    df.columns = (df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_', regex=False)
        .str.replace('/', '_', regex=False))

    # Price
    if 'price' in df.columns:
        df['price_gbp'] = clean_price(df['price'])

    # Host flags
    for col in ['host_is_superhost', 'instant_bookable']:
        if col in df.columns:
            df[col + '_bin'] = booleanize(df[col])

    # Host tenure
    if 'host_since' in df.columns:
        df['host_since'] = pd.to_datetime(df['host_since'], errors='coerce')
        df['host_tenure_days'] = (pd.Timestamp.today().normalize() - df['host_since']).dt.days

    # Amenities count
    if 'amenities' in df.columns:
        df['amenity_count'] = df['amenities'].fillna('[]').astype(str).str.count(',') + 1
        df.loc[df['amenities'].isna(), 'amenity_count'] = 0

    # Minimum nights, availability
    for col in ['minimum_nights', 'availability_365', 'number_of_reviews', 'review_scores_rating']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Drop impossible or extreme prices (basic sanity)
    if 'price_gbp' in df.columns:
        df = df[df['price_gbp'].between(10, 1000)]  # adjust if needed

    to_csv(df, args.output, index=False)
    print(f"✅ Saved cleaned data to {args.output} (rows: {len(df)})")

if __name__ == '__main__':
    main()
