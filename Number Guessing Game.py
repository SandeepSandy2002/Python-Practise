'''3.Number Guessing Game
   - Develop a program where the computer generates a random number between 1 and 100, and the user guesses the number.
   - Provide hints like "Too High" or "Too Low."
   - Use a loop to allow multiple attempts.'''

import random
#print(random.randint(1,100))
num = random.randint(1,100)
while True:
  #print(num)
   if num<50:
      msg = "less"
   else:
      msg= "greater"
   user = int(input(f"Guess the number which is { msg } than 50: "))
   if user == num:
      print(" you won")
      break
   else:
      print(f"try again")