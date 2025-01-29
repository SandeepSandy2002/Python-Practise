'''12. Pattern Generator
   - Create a program that generates the following pattern based on user input `n`:
     *
     **
     ***
     ****
   - Add an option to print the pattern in reverse.'''

num = int(input())
for i in range(1 , num+1):
    print("*"*i)