from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///bluestock_mf.db')

PROCESSED = 'data/processed'

tables = {
    'dim_fund': '01_fund_master_clean.csv',
    'fact_nav': '02_nav_history_clean.csv',
    'fact_aum': '03_aum_clean.csv',
    'fact_transactions': '08_investor_transactions_clean.csv',
    'fact_performance': '07_scheme_performance_clean.csv',
}

for table, file in tables.items():
    try:
        df = pd.read_csv(f'{PROCESSED}/{file}')
        df.to_sql(table, engine, if_exists='replace', index=False)
        print(f'Loaded: {table} - {len(df)} rows')
    except Exception as e:
        print(f'Error {table}: {e}')

print('Star schema loaded!')
