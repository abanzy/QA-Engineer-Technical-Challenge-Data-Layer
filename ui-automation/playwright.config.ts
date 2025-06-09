import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    baseURL: 'http://localhost:3000',
    headless: true,
    trace: 'on',
  },
  testDir: './playwright',
  reporter: [['html', { outputFolder: 'playwright-report' }], ['list']],
});
