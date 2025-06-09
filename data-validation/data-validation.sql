-- 1. Assert record counts match between staging and prod, with details
SELECT
    IFF(
        (SELECT COUNT(*) FROM staging.transactions) = (SELECT COUNT(*) FROM prod.transactions),
        'PASS',
        'FAIL - Staging count: ' || (SELECT COUNT(*) FROM staging.transactions)::VARCHAR ||
        ', Prod count: ' || (SELECT COUNT(*) FROM prod.transactions)::VARCHAR
    ) AS record_count_match;

-- 2. Assert no negative amounts in prod.transactions, with details
SELECT
    IFF(
        (SELECT COUNT(*) FROM prod.transactions WHERE amount < 0) = 0,
        'PASS',
        'FAIL - Negative amounts found: ' || (SELECT COUNT(*) FROM prod.transactions WHERE amount < 0)::VARCHAR
    ) AS no_negative_amounts;

-- 3. Assert no missing transaction_id in prod.transactions, with details
SELECT
    IFF(
        (SELECT COUNT(*) FROM prod.transactions WHERE transaction_id IS NULL OR transaction_id = '') = 0,
        'PASS',
        'FAIL - Missing transaction_id values found: ' || (SELECT COUNT(*) FROM prod.transactions WHERE transaction_id IS NULL OR transaction_id = '')::VARCHAR
    ) AS no_missing_transaction_id;
