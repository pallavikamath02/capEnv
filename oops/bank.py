class Bank:
    def __init__(self):
        self.accounts = {}

    def __create_account(self, account_id, initial_balance=0):
        if account_id in self.accounts:
            print("Account already exists.")
            return
        self.accounts[account_id] = initial_balance

    def _deposit(self, account_id, amount):
        if account_id not in self.accounts:
            print("Account does not exist.")
            return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.accounts[account_id] += amount

    def _withdraw(self, account_id, amount):
        if account_id not in self.accounts:
            print("Account does not exist.")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.accounts[account_id] < amount:
            print("Insufficient funds.")
            return
        self.accounts[account_id] -= amount

    def __get_balance(self, account_id):
        if account_id not in self.accounts:
            print("Account does not exist.")
            return None
        return self.accounts[account_id]
    
if __name__ == "__main__":
    bank = Bank()
    bank._Bank__create_account("12345", 1000)
    bank._deposit("12345", 500)
    bank._withdraw("12345", 200)
    balance = bank._Bank__get_balance("12345")
    print(f"Account 12345 balance: {balance}")