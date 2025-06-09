const express = require('express');
const app = express();
app.use(express.urlencoded({ extended: true }));

app.get('/login', (req, res) => {
  res.send(`
    <form action="/dashboard" method="get">
      <input name="username" />
      <input name="password" type="password" />
      <button type="submit">Login</button>
    </form>
  `);
});

app.get('/dashboard', (req, res) => {
  res.send(`
    <table>
      <thead>
        <tr>
          <th>Transaction ID</th>
          <th>Amount</th>
          <th>Currency</th>
          <th>Timestamp</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>abc123</td>
          <td>100</td>
          <td>USD</td>
          <td>2025-06-08T12:00:00Z</td>
        </tr>
        <tr>
          <td>def456</td>
          <td>200</td>
          <td>BRL</td>
          <td>2025-06-08T13:00:00Z</td>
        </tr>
      </tbody>
    </table>
  `);
});

app.listen(3000, () => console.log('Mock UI server running on http://localhost:3000'));
