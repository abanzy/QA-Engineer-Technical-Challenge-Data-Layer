
import { test, expect } from '@playwright/test';
import { DashboardPage } from './dashboard.page';

test.describe('Dashboard UI', () => {
  test.beforeEach(async ({ page }) => {
    // Mocked login API
    await page.route('**/api/login', route => {
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ token: 'mock-token' })
      });
    });
    // Mocked transactions API
    await page.route('**/api/transactions', route => {
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          transactions: [
            { transaction_id: 'abc123', amount: 100, currency: 'USD', timestamp: '2025-06-08T12:00:00Z' },
            { transaction_id: 'def456', amount: 200, currency: 'BRL', timestamp: '2025-06-08T13:00:00Z' }
          ]
        })
      });
    });
  });

  test('Validates Login flow storing tokens', async ({ page }) => {
    const dashboard = new DashboardPage(page);
    await dashboard.gotoLogin();
    await dashboard.login('testuser', 'password');
    await expect(page).toHaveURL(/\/dashboard(\?.*)?$/);
  });

  test('Validates Table headers and row content', async ({ page }) => {
    const dashboard = new DashboardPage(page);
    await dashboard.gotoDashboard();
    const headers = await dashboard.getHeaders();
    expect(headers).toEqual([
      'Transaction ID',
      'Amount',
      'Currency',
      'Timestamp'
    ]);
    const rowCount = await dashboard.getRowCount();
    expect(rowCount).toBe(2);
    const currencies = await dashboard.getCurrencies();
    for (const currency of currencies) {
      expect(['USD', 'BRL']).toContain(currency);
    }
  });
});
