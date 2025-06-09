# Mock UI Server

This is a simple Express.js server that provides mock UI endpoints for QA and UI automation testing.

## Endpoints

- **GET `/login`**
  - Returns a login form with username and password fields.
  - Submits to `/dashboard` via GET.

- **GET `/dashboard`**
  - Returns a static HTML table with two hardcoded transactions.
  - Table columns: Transaction ID, Amount, Currency, Timestamp.
  - Example rows:
    - `abc123`, `100`, `USD`, `2025-06-08T12:00:00Z`
    - `def456`, `200`, `BRL`, `2025-06-08T13:00:00Z`


## Usage

### 1. Install dependencies
```bash
npm install express
```

### 2. Run the server
```bash
node mock_ui_server.js
```

### 3. Access the UI
- Login page: [http://localhost:3000/login](http://localhost:3000/login)
- Dashboard: [http://localhost:3000/dashboard](http://localhost:3000/dashboard)

---

## Running UI Automation Tests

You can run the Playwright UI tests against this mock server.

1. **Start the mock UI server** (see above).
2. **In a separate terminal, run:**
   ```bash
   npx playwright test
   ```
   Or use the VS Code task: **Run UI Tests (Playwright)**

This will execute the Playwright tests in `dashboard.spec.ts` against the running mock UI server.

## Purpose

- Use this server as a mock frontend for UI automation tests (e.g., with Playwright).
- The static table is designed to match the expected structure for automated validation.

---

**Note:** This server is for local development and testing only. Do not use in production.
