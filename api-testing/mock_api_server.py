from flask import Flask, jsonify

app = Flask(__name__)

# Expanded mock data with more transactions, no negative values and multiple currencies for the sake of it
MOCK_TRANSACTIONS = [
    {"transaction_id": "abc123", "amount": 100, "currency": "USD", "timestamp": "2025-06-08T12:00:00Z"},
    {"transaction_id": "def456", "amount": 200, "currency": "BRL", "timestamp": "2025-06-08T13:00:00Z"},
    {"transaction_id": "ghi789", "amount": 50, "currency": "EUR", "timestamp": "2025-06-08T14:00:00Z"},
    {"transaction_id": "jkl012", "amount": 10, "currency": "GBP", "timestamp": "2025-06-08T15:00:00Z"},
    {"transaction_id": "mno345", "amount": 0, "currency": "INR", "timestamp": "2025-06-08T16:00:00Z"},
    {"transaction_id": "pqr678", "amount": 500, "currency": "AUD", "timestamp": "2025-06-08T17:00:00Z"}
]

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    return jsonify({"transactions": MOCK_TRANSACTIONS}), 200

@app.route('/api/transactions/<tid>', methods=['GET'])
def get_transaction_by_id(tid):
    for t in MOCK_TRANSACTIONS:
        if t["transaction_id"] == tid:
            return jsonify(t), 200
    return jsonify({"error": "Bad Request"}), 400

@app.route('/api/transactions/delete/<tid>', methods=['DELETE'])
def delete_transaction(tid):
    for t in MOCK_TRANSACTIONS:
        if t["transaction_id"] == tid:
            return jsonify({"success": True}), 200
    return jsonify({"error": "Bad Request"}), 400

if __name__ == '__main__':
    app.run(port=5000)