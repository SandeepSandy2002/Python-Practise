'''11. Password Strength Checker
   - Develop a program to check the strength of a password:
     - Criteria: At least 8 characters, includes uppercase, lowercase, digits, and special characters.'''

def password_checker():
  while True:
   password = input("enter the password : ")

   if len(password) < 8:
      print(" Week : length should be more then 8")
   u = l = d = s = 0
   for i in password:
      if i.isupper():
         u += 1
      elif i.islower():
         l += 1
      elif i.isnumeric():
         d += 1
      else:
         s += 1
   if u == 0:
      print(" Week : no uppercase")
   elif l == 0:
      print(" Week : no lowercase")
   elif d == 0:
      print(" Week : no digits")
   elif s == 0:
      print(" Week : no special characters")
   else :
      print(" Strong password")
      break
def main():
   password_checker()
main()