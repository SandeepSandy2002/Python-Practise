'''Multiplication Table Generator
    -Create a program to generate a multiplication table for any number provided by the user.
   - Allow the user to specify the range of the table.'''

def main():
   num , limit = map(int , input("enter the number and the range with space between them ").split())
   for i in range(1,limit+1):
      print(f"{num} x {i} = {num*i}")
main()