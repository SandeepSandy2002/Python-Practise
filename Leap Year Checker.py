'''15. Leap Year Checker
   - Write a program to check if a given year is a leap year.
   - Allow the user to check multiple years.'''

while True:
  choice = int(input("enter the year to check 0. to exit"))
  if choice == 0:
    break
  else:
    if choice % 4 == 0 and choice % 100 == 0:
      print(f"{choice} is a leap year")
    else:
      print(f"{choice} is not a leap year")