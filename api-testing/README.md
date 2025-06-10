# API Testing with Postman & Newman

This folder contains automated API tests for the Transaction API (e.g., Snowflake data warehouse) using Postman collections and Newman for CLI automation.

## What is tested?
- **Response status codes:** 200, 400, 500
- **Response schema:** Each transaction must have `transaction_id`, `amount`, `currency`, and `timestamp` fields
- **Business rule:** Amount cannot be negative

## Files
- `api-tests.postman_collection.json` — The Postman collection with all API test cases and scripts
- `mock-environment.json` — Postman environment file (sets `baseUrl`)
- `run.sh` — Bash script to run all tests and generate reports (Linux/macOS/Git Bash)

## How it works
- The Postman collection sends requests to the Transaction API endpoints (GET, GET by ID, DELETE)
- Test scripts in the collection validate status codes, required fields, and business rules
- Newman runs the collection and outputs CLI, HTML, and JSON reports to the `../reports` directory

## How to run

### 1. Start your mock API server
Make sure your API server (e.g., `mock_api_server.py`) is running and accessible at the base URL in `mock-environment.json` (default: `http://localhost:5000`).

### 2. Install Newman (if not already installed)
```bash
npm install -g newman
```

### 3. Run the tests (from this folder)
```bash
bash run.sh
```

- Reports will be generated in the `../reports` directory.
- You can also run the collection manually:
  ```bash
  newman run api-tests.postman_collection.json -e mock-environment.json
  ```

## Reports
- CLI output: summary in terminal
- HTML: `../reports/newman-report.html`
- JSON: `../reports/newman-report.json`

---

**Note:**
- Make sure the API server is running before executing the tests.
- Update `mock-environment.json` if your API base URL changes.
