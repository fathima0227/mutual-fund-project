import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RAW_DATA_PATH = 'data/raw'
PROCESSED_DATA_PATH = 'data/processed'

def load_all_csv():
    all_dataframes = []
    for file in os.listdir(RAW_DATA_PATH):
        if file.endswith('.csv'):
            filepath = os.path.join(RAW_DATA_PATH, file)
            df = pd.read_csv(filepath)
            df['source_file'] = file
            all_dataframes.append(df)
            logger.info(f'Loaded: {file}')
    return all_dataframes

def save_processed(df, filename='combined_data.csv'):
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    output_path = os.path.join(PROCESSED_DATA_PATH, filename)
    df.to_csv(output_path, index=False)

if __name__ == '__main__':
    dataframes = load_all_csv()
    combined = pd.concat(dataframes, ignore_index=True)
    save_processed(combined)
    print('Data ingestion complete!')
