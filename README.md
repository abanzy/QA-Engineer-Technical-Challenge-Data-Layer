
# QA Test Project

This repository contains a comprehensive QA technical challenge covering:
- **API Testing** (Postman + Newman)
- **UI Automation** (Playwright)
- **LLM/Chatbot Testing** (Prompt Validation + LLM judge  + SBERT sample)
- **Data Validation** (SQL)
- **CI/CD Automation** (GitHub Actions)

---

## Structure

- `api-testing/` — Automated API tests (Postman collection, environment, run script, and README)
- `ui-automation/` — Playwright UI automation tests, mock UI server, config, and README
- `llm-chatbot/` — LLM/Chatbot validation scripts, mock API, test strategy, and README
- `data-validation/` — SQL scripts for data validation and README
- `reports/` — Test and validation reports (HTML, JSON)
- `.github/workflows/qa-pipeline.yml` — CI/CD pipeline
- `run.sh` — Root scripts for running tests (see subfolders for details)

---

## How to Run

### 1. API Tests (Postman + Newman)
- Go to `Project/api-testing/`.
- Start your mock API server (see LLM/Chatbot section if needed).
- Run tests:
  ```bash
  bash run.sh
  ```
- Reports are generated in `../reports/`.
- See `api-testing/README.md` for details.

### 2. UI Automation (Playwright)
- Go to `Project/ui-automation/`.
- Install dependencies:
  ```bash
  npm install
  ```
- Start the mock UI server:
  ```bash
  node playwright/mock_ui_server.js
  ```
- Run UI tests:
  ```bash
  npx playwright test
  ```
- Reports are generated in `playwright-report/`.
- See `ui-automation/README.md` for details.

### 3. LLM/Chatbot Testing
- Go to `Project/llm-chatbot/`.
- Start the mock chatbot API:
  ```bash
  python mock_chatbot_api.py
  ```
- Run the LLM validation script:
  ```bash
  python llm_test_script.py
  ```
- See `llm-chatbot/llm-test-strategy.md` for details.

### 4. Data Validation (SQL)
- Go to `Project/data-validation/`.
- Open `data-validation.sql` in your Snowflake worksheet or compatible SQL client.
- Run the queries to validate data integrity and business rules.
- See `data-validation/README.md` for details and output examples.

### 5. CI/CD Pipeline
- Automated pipeline runs on push/PR via `.github/workflows/qa-pipeline.yml`.

---

## Notes
- All scripts and tests are organized by function for clarity and maintainability.
- See each subfolder's `README.md` for detailed instructions and context.
- All deliverables are designed to match the provided technical challenge specification and checklists.
