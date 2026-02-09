a = 1
b = 100
print('Prime numbers less than 20 are:')
for num in range(a, b + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end=' ')
def fib(n):
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
print("\n")
print("Fibonacci series")
fib(100)
