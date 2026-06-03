# Data Dictionary - Bluestock Fintech Mutual Fund Project

## 1. fund_master
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INT | Unique fund identifier |
| fund_name | TEXT | Name of the mutual fund |
| category | TEXT | Fund category |
| amc_name | TEXT | Asset Management Company |

## 2. nav_history
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INT | Fund identifier |
| date | DATE | NAV date |
| nav | FLOAT | Net Asset Value |

## 3. scheme_performance
| Column | Type | Description |
|--------|------|-------------|
| fund_name | TEXT | Fund name |
| returns_1yr | FLOAT | 1 year returns % |
| expense_ratio | FLOAT | Annual expense ratio % |

## 4. investor_transactions
| Column | Type | Description |
|--------|------|-------------|
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount | FLOAT | Transaction amount |
| date | DATE | Transaction date |
