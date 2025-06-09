from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    prompt = request.json.get('prompt', '').lower()
    import random

    # Transaction-related prompts: always return a human-like message
    if 'txn' in prompt or 'transaction' in prompt:
        responses = [
            {"message": "Hi! Here are your most recent transactions:\n\n- $100 USD on June 8, 2025 at 12:00 UTC (ID: abc123)\n- R$200 BRL on June 8, 2025 at 13:00 UTC (ID: def456)\n\nTotal: $300. Let me know if you want more details or something else!"},
            {"message": "You have 5 transactions:\n\n1. $100 USD on June 8, 2025 at 12:00 UTC (abc123)\n2. R$200 BRL on June 8, 2025 at 13:00 UTC (def456)\n3. €150 EUR on June 8, 2025 at 14:00 UTC (ghi789)\n4. £50 GBP on June 8, 2025 at 15:00 UTC (jkl012)\n5. $250 USD on June 8, 2025 at 16:00 UTC (mno345)\n\nTotal: $750. Would you like a summary or details for each?"},
            {"message": "Looks like you don't have any transactions yet. If you need help getting started, just ask!"},
            {"message": "I checked everywhere, but couldn't find any transactions. Maybe try again later or ask for something else?"},
            {"message": "Here are your latest transactions!\n\n- $100 USD on June 8, 2025 at 12:00 UTC (abc123)\n- R$200 BRL on June 8, 2025 at 13:00 UTC (def456)\n\nTotal: $300. If you want to filter by date or amount, let me know."}
        ]
        return jsonify(random.choice(responses))

    # Mars or invalid location: always return a message key
    if 'mars' in prompt:
        return jsonify({"message": "Sorry, I can't find any transactions from Mars. Please ask about your Earth accounts!"})

    # All other prompts: generic fallback
    return jsonify({"message": "I'm not sure how to help with that. Try asking about your transactions or account balance!"})

if __name__ == '__main__':
    app.run(port=5001)
