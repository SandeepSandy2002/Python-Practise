'''14. Factorial Calculator
   - Create a program to calculate the factorial of a number using a loop.
   - Include error handling for negative numbers.'''

num = int(input("Enter the number : "))
fact = 1
if num<0:
  print("enter the positive number")
elif num == 0:
  print(1)
else:
  for i in range(1,num+1):
    fact *= i
  print(fact)