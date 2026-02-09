class xyz:
	def __init__(self,name,age, pancard, adharcard,address,phone_number): 
		self.age=age 		
		self.name=name 
		self.pancard=pancard
		self.adharcard=adharcard
		self.address=address
		self.phone_number=phone_number 
		
name=input("enter the name: ")
age=input("enter your age: ")
pancard=input("enter the pancard number: ")
adharcard=input("enter the adhar number: ")
address=input("enter your address: ")
phone_number=input("enter your phone number: ")

dog1=xyz(name,age,pancard,adharcard,address,phone_number) #object creation
print(dog1.name)
print(dog1.age)
print(dog1.address)
print(dog1.pancard)
print(dog1.adharcard)
print(dog1.phone_number)
