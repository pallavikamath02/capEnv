class Bankaccount:
    def __init__(self):
        self.amount=1000
    
    def withdrwal(self,amt):
        if amt>self.amount:
            return "Insufficient balance"
        else:
            self.amount-=amt
            return f"Withdrawal successful! Remaining balance: {self.amount}"
    #private method
    def __update__(self,amt):
        self.amount=amt
        return f"Account updated! New balance: {self.amount}"
    def _deposit_(self,amt):
        self.amount+=amt
        return f"Deposit successful! New balance: {self.amount}"    
    
    #protected methid
    def _show_details_(self):
        return f"Current balance: {self.amount}"

acc=Bankaccount()
acc.withdrwal(500)
acc.__update__(3000)   
print(acc._deposit_(2000))
print(acc._show_details_())
print(acc.__update__(3000)) #private method cannot be accessed outside the class
print(acc.withdrwal(500))  
print(acc._show_details_())