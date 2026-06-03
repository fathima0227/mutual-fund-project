import pandas as pd
import os

RAW = 'data/raw'
PROCESSED = 'data/processed'
os.makedirs(PROCESSED, exist_ok=True)

# Fix missing 2 files
files = {
    '03_aum_by_fund_house.csv': '03_aum_clean.csv',
    '04_monthly_sip_inflows.csv': '04_sip_clean.csv'
}

for raw, clean in files.items():
    try:
        df = pd.read_csv(f'{RAW}/{raw}', encoding='utf-8', on_bad_lines='skip')
        df = df.drop_duplicates()
        df = df.dropna(how='all')
        df.to_csv(f'{PROCESSED}/{clean}', index=False)
        print(f'Cleaned: {raw} - {len(df)} rows')
    except Exception as e:
        print(f'Error: {e}')

print('DONE!')
