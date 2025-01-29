'''13. Palindrome Checker
   - Write a program to check if a given string or number is a palindrome.
   - Allow the user to input multiple values using a loop.'''

def palindrome_string():

   string=input('enter the string: ')
   if string == string[::-1]:
      print(f'{string} is a palindrome ')
   else:
      print(f'{string} is not a palindrome')

def palindrome_number():
    number = int(input("enter the number : "))
    rev = 0
    dup = number
    while dup:
      rem = dup % 10
      rev = rev * 10 + rem
      dup //= 10
    if number == rev:
      print(f"{number} is a palindrome")
    else:
      print(f"{number} is not a palindrome")

def get_input():
   while True:
      choice=int(input('choose an option \n1.string \n2.number \n3.exit\n'))
      if choice==1:
         palindrome_string()
      elif choice==2:
         palindrome_number()
      else:
         print("Thank you!")
         break
def main():
   get_input()
main()