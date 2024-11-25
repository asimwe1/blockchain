from flask import Flask, jsonify
from web3 import Web3

app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # Local Ganache instance

@app.route('/balance/<address>', methods=['GET'])
def get_balance(address):
    balance = w3.eth.get_balance(address)
    return jsonify({"balance": balance})

if __name__ == '__main__':
    app.run(debug=True)
