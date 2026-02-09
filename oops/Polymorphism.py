class Calculator:
    def multiply(self, a=1,b=1,*args):
        resu=a*b
        for n in args:
            resu*=n
            return resu
        
calc=Calculator()
#using default arguments
print(calc.multiply())
print(calc.multiply(4))

#using Multiple arguments
print(calc.multiply(2,3))
print(calc.multiply(2,3,4))