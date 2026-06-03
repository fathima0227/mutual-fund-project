-- schema.sql
CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_name TEXT,
    category TEXT,
    amc_name TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id INTEGER PRIMARY KEY,
    date DATE,
    month INTEGER,
    year INTEGER
);

CREATE TABLE IF NOT EXISTS fact_nav (
    id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date DATE,
    nav FLOAT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount FLOAT,
    date DATE,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE IF NOT EXISTS fact_performance (
    id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    returns_1yr FLOAT,
    returns_3yr FLOAT,
    expense_ratio FLOAT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE IF NOT EXISTS fact_aum (
    id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    aum FLOAT,
    date DATE,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);
