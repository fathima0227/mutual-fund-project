import pandas as pd
import sqlite3
import os

PROCESSED = 'data/processed'
conn = sqlite3.connect('bluestock_mf.db')

files = {
    'fund_master': '01_fund_master_clean.csv',
    'nav_history': '02_nav_history_clean.csv',
    'aum': '03_aum_clean.csv',
    'sip': '04_sip_clean.csv',
    'category_inflows': '05_category_inflows_clean.csv',
    'folio_count': '06_industry_folio_count_clean.csv',
    'scheme_performance': '07_scheme_performance_clean.csv',
    'transactions': '08_investor_transactions_clean.csv',
    'portfolio': '09_portfolio_holdings_clean.csv',
    'benchmark': '10_benchmark_indices_clean.csv'
}

for table, file in files.items():
    try:
        df = pd.read_csv(f'{PROCESSED}/{file}')
        df.to_sql(table, conn, if_exists='replace', index=False)
        print(f'Loaded: {table} - {len(df)} rows')
    except Exception as e:
        print(f'Error {table}: {e}')

conn.close()
print('Database bluestock_mf.db created!')
