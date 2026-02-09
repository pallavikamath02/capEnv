class Bank:
    bank="Swiss Bank"
    def __init__(self,name,age,ano,pno,phno,adrs):
        self.name = name
        self.age = age
        self.ano = ano
        self.pno = pno
        self.phno = phno
        self.adrs = adrs
        
name = input("Enter your name:")
age = int(input("Enter your age:"))
ano = input("Enter your Aadhaar number:")
pno = input("Enter your PAN Card number:")
phno = input("Enter your Phone Number:")
adrs = input("Enter your address:") 

name1 = Bank(name,age,ano,pno,phno,adrs)
print(name1.name)
print(name1.age)
print(name1.ano)   
print(name1.pno)
print(name1.phno)
print(name1.adrs)