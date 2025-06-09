# Data Validation SQL for Snowflake

This folder contains SQL scripts to validate the integrity and quality of transaction data between staging and production tables in Snowflake.

## What is validated?

1. **Record Count Match**
   - Compares the number of records in `staging.transactions` and `prod.transactions`.
   - Returns `PASS` if counts match, otherwise returns `FAIL` with the actual counts.

2. **No Negative Amounts**
   - Checks that there are no negative `amount` values in `prod.transactions`.
   - Returns `PASS` if none found, otherwise returns `FAIL` with the count of negative amounts.

3. **No Invalid or Missing `transaction_id`**
   - Checks for `NULL`, empty, whitespace-only, or `'NaN'` (case-insensitive) `transaction_id` values in `prod.transactions`.
   - Returns `PASS` if none found, otherwise returns `FAIL` with the count of invalid IDs.

## How to use

1. Open your Snowflake worksheet or SQL client.
2. Run the queries in `data-validation.sql`.
3. Review the output:
   - Each query returns `PASS` or a detailed `FAIL` message.

## Example Output
| record_count_match | no_negative_amounts | no_invalid_transaction_id |
|--------------------|--------------------|--------------------------|
| PASS               | PASS               | PASS                     |

Or, if issues are found:
| record_count_match | no_negative_amounts | no_invalid_transaction_id |
|--------------------|--------------------|--------------------------|
| FAIL - Staging count: 100, Prod count: 98 | FAIL - Negative amounts found: 2 | FAIL - Invalid transaction_id values found: 1 |

## Notes
- You can add more checks as needed (e.g., duplicate IDs, date range validation).
- These queries are designed for Snowflake but can be adapted for other SQL engines.
- Make sure you have access to both `staging.transactions` and `prod.transactions` tables.

---

**Contact your data engineering or QA team for more advanced validation needs.**
