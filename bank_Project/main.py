from flask import Flask, request, jsonify, redirect
from flasgger import Swagger
import datetime

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/swagger-ui')
def swagger_ui_redirect():
    return redirect('/apidocs')

# --- Models ---
class Customer:
    def __init__(self, customer_id, name, email, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number
        }

class Account:
    def __init__(self, account_number, customer_id, account_type, balance=0.0):
        self.account_number = account_number
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "customer_id": self.customer_id,
            "account_type": self.account_type,
            "balance": self.balance
        }

class Transaction:
    def __init__(self, transaction_id, account_number, transaction_type, amount, date=None):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date if date else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "account_number": self.account_number,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "date": self.date
        }

# --- In-memory Storage ---
customers = []
accounts = []
transactions = []

# --- Routes ---

@app.route('/customers', methods=['POST'])
def create_customer():
    """
    Create a new customer
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            customer_id:
              type: string
            name:
              type: string
            email:
              type: string
            phone_number:
              type: string
    responses:
      201:
        description: Customer created successfully
      400:
        description: Customer ID already exists
    """
    data = request.get_json()
    c_id = data.get('customer_id')
    
    if any(c.customer_id == c_id for c in customers):
        return jsonify({"error": "Customer ID already exists!"}), 400
        
    customer = Customer(c_id, data.get('name'), data.get('email'), data.get('phone_number'))
    customers.append(customer)
    return jsonify({"message": "Customer created successfully!", "customer": customer.to_dict()}), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    """
    List all customers
    ---
    responses:
      200:
        description: List of customers
    """
    return jsonify([c.to_dict() for c in customers])

@app.route('/accounts', methods=['POST'])
def create_account():
    """
    Create a new account
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            account_number:
              type: string
            customer_id:
              type: string
            account_type:
              type: string
              enum: [Savings, Current]
            balance:
              type: number
    responses:
      201:
        description: Account created successfully
      400:
        description: Error creating account
    """
    data = request.get_json()
    a_num = data.get('account_number')
    c_id = data.get('customer_id')
    
    if not any(c.customer_id == c_id for c in customers):
        return jsonify({"error": "Customer ID not found!"}), 400
    if any(a.account_number == a_num for a in accounts):
        return jsonify({"error": "Account Number already exists!"}), 400
        
    account = Account(a_num, c_id, data.get('account_type'), data.get('balance', 0.0))
    accounts.append(account)
    return jsonify({"message": "Account created successfully!", "account": account.to_dict()}), 201

@app.route('/accounts', methods=['GET'])
def get_accounts():
    """
    List all accounts
    ---
    responses:
      200:
        description: List of accounts
    """
    return jsonify([a.to_dict() for a in accounts])

@app.route('/transactions', methods=['POST'])
def perform_transaction():
    """
    Perform a transaction (Deposit/Withdraw)
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            transaction_id:
              type: string
            account_number:
              type: string
            transaction_type:
              type: string
              enum: [Deposit, Withdraw]
            amount:
              type: number
    responses:
      201:
        description: Transaction successful
      400:
        description: Transaction failed
    """
    data = request.get_json()
    t_id = data.get('transaction_id')
    a_num = data.get('account_number')
    t_type = data.get('transaction_type')
    amount = data.get('amount')
    
    account = next((a for a in accounts if a.account_number == a_num), None)
    if not account:
        return jsonify({"error": "Account not found!"}), 400
        
    success = False
    if t_type == 'Deposit':
        success = account.deposit(amount)
    elif t_type == 'Withdraw':
        success = account.withdraw(amount)
    else:
        return jsonify({"error": "Invalid transaction type"}), 400
        
    if success:
        transaction = Transaction(t_id, a_num, t_type, amount)
        transactions.append(transaction)
        return jsonify({
            "message": "Transaction successful",
            "new_balance": account.balance,
            "transaction": transaction.to_dict()
        }), 201
    else:
        return jsonify({"error": "Transaction failed (Insufficient funds or invalid amount)"}), 400

@app.route('/transactions', methods=['GET'])
def get_transactions():
    """
    List all transactions
    ---
    responses:
      200:
        description: List of transactions
    """
    return jsonify([t.to_dict() for t in transactions])

if __name__ == "__main__":
    app.run(debug=True)
