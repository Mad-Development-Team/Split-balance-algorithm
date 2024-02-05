from flask import Flask, request, jsonify
from Split import Split

app = Flask(__name__)

@app.route('/balance', methods=['POST'])
def balance():
    data = request.json
    if not data or 'expenses' not in data:
        return jsonify({'error': 'Bad request, missing expenses data'}), 400

    expenses = data['expenses']
    split_instance = Split(expenses)
    transactions = split_instance.balance()

    formatted_transactions = [[trans[0], trans[1], trans[2]] for trans in transactions]

    return jsonify({"balance": formatted_transactions})


if __name__ == '__main__':
    app.run()
