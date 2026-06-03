-- queries.sql
-- 1. Top 5 funds by AUM
SELECT fund_name, aum FROM aum ORDER BY aum DESC LIMIT 5;

-- 2. Average NAV per month
SELECT strftime('%Y-%m', date) as month, AVG(nav) as avg_nav FROM nav_history GROUP BY month;

-- 3. Total transactions by type
SELECT transaction_type, COUNT(*) as count FROM transactions GROUP BY transaction_type;

-- 4. Funds with expense ratio less than 1%
SELECT * FROM scheme_performance WHERE expense_ratio < 1;

-- 5. SIP growth over time
SELECT * FROM sip ORDER BY date;

-- 6. Top 10 benchmark indices
SELECT * FROM benchmark LIMIT 10;

-- 7. Category inflows total
SELECT category, SUM(inflow) as total FROM category_inflows GROUP BY category;

-- 8. Portfolio holdings count
SELECT COUNT(*) as total FROM portfolio;

-- 9. Folio count by industry
SELECT * FROM folio_count ORDER BY folio_count DESC;

-- 10. Scheme performance average returns
SELECT AVG(returns_1yr) as avg_1yr FROM scheme_performance;
