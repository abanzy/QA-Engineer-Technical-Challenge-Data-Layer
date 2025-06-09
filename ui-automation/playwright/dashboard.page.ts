import { Page, Locator } from '@playwright/test';

export class DashboardPage {
  readonly page: Page;
  readonly usernameInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly tableHeaders: Locator;
  readonly tableRows: Locator;
  readonly currencyCells: Locator;

  constructor(page: Page) {
    this.page = page;
    this.usernameInput = page.locator('input[name="username"]');
    this.passwordInput = page.locator('input[name="password"]');
    this.loginButton = page.locator('button[type="submit"]');
    this.tableHeaders = page.locator('table thead tr th');
    this.tableRows = page.locator('table tbody tr');
    this.currencyCells = page.locator('table tbody tr td:nth-child(3)'); // I know this is bad practice, but it's for a demo mocked by myself
  }

  async gotoLogin() {
    await this.page.goto('/login');
  }

  async login(username: string, password: string) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async gotoDashboard() {
    await this.page.goto('/dashboard');
  }

  async getHeaders() {
    return this.tableHeaders.allTextContents();
  }

  async getRowCount() {
    return this.tableRows.count();
  }

  async getCurrencies() {
    return this.currencyCells.allTextContents();
  }
}
