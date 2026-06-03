import pandas as pd
import os

RAW = 'data/raw'
PROCESSED = 'data/processed'
os.makedirs(PROCESSED, exist_ok=True)

files = [
    '01_fund_master.csv',
    '02_nav_history.csv',
    '03_aum_by_house.csv',
    '04_monthly_sip_info.csv',
    '05_category_inflows.csv',
    '06_industry_folio_count.csv',
    '07_scheme_performance.csv',
    '08_investor_transactions.csv',
    '09_portfolio_holdings.csv',
    '10_benchmark_indices.csv'
]

for file in files:
    try:
        df = pd.read_csv(f'{RAW}/{file}', encoding='utf-8', on_bad_lines='skip')
        df = df.drop_duplicates()
        df = df.dropna(how='all')
        clean_name = file.replace('.csv', '_clean.csv')
        df.to_csv(f'{PROCESSED}/{clean_name}', index=False)
        print(f'Cleaned: {file} - {len(df)} rows')
    except Exception as e:
        print(f'Error in {file}: {e}')

print('DONE!')
