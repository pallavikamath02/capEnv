from flask import Flask, jsonify, request

app = Flask(__name__)

accounts = {
    1: {
        "username": "aditya", "password": "123",
        "acc_no": "ACC1001",
        "name": "Aditya Kumar",
        "balance": 50000,
        "salary": 35000,
        "account_type": "Savings",
        "aadhar": "111122223333",
        "pan": "ABCDE1234F",
        "phone": "9999999999"
    },
    2: {
        "username": "rahul", "password": "123",
        "acc_no": "ACC1002",
        "name": "Rahul Sharma",
        "balance": 20000,
        "salary": 25000,
        "account_type": "FD",
        "aadhar": "444455556666",
        "pan": "PQRSX5678L",
        "phone": "8888888888"
    }
}

@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Send JSON only"}), 415

    data = request.get_json()

    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    for uid, user in accounts.items():
        if user["username"] == username and user["password"] == password:
            return jsonify({
                "message": "Login successful",
                "user_id": uid
            }), 200

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = accounts.get(user_id)
    if not user:
        return jsonify({"error": "Account not found"}), 404

    result = user.copy()
    result.pop("password")
    result["loan_eligible"] = result["salary"] >= 30000
    return jsonify(result), 200


@app.route("/users", methods=["GET"])
def get_all_users():
    result = {}
    for uid, user in accounts.items():
        temp = user.copy()
        temp.pop("password")
        temp["loan_eligible"] = temp["salary"] >= 30000
        result[uid] = temp
    return jsonify(result), 200


@app.route("/account", methods=["POST"])
def create_account():
    data = request.get_json()
    required_fields = [
        "user_id", "username", "password", "acc_no", "name",
        "balance", "salary", "account_type", "aadhar", "pan", "phone"
    ]

    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    user_id = data["user_id"]
    if user_id in accounts:
        return jsonify({"error": "User already exists"}), 400

    accounts[user_id] = {
        "username": data["username"],
        "password": data["password"],
        "acc_no": data["acc_no"],
        "name": data["name"],
        "balance": data["balance"],
        "salary": data["salary"],
        "account_type": data["account_type"],
        "aadhar": data["aadhar"],
        "pan": data["pan"],
        "phone": data["phone"]
    }

    return jsonify({"message": "Account created successfully"}), 201


@app.route("/account/<int:user_id>", methods=["PUT"])
def update_balance(user_id):
    user = accounts.get(user_id)
    if not user:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json()
    if not data or "amount" not in data:
        return jsonify({"error": "Amount required"}), 400

    amount = data["amount"]
    if user["balance"] + amount < 0:
        return jsonify({"error": "Insufficient balance"}), 400

    user["balance"] += amount
    return jsonify({
        "message": "Balance updated",
        "new_balance": user["balance"]
    }), 200


@app.route("/account/<int:user_id>", methods=["DELETE"])
def delete_account(user_id):
    if user_id not in accounts:
        return jsonify({"error": "Account not found"}), 404

    del accounts[user_id]
    return jsonify({"message": "Account deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)