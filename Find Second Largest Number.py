'''19. Find Second Largest Number
   - Write a program to find the second largest number in a list provided by the user.'''

def main():
    print('enter the numbers:')
    numbers = list(map(int, input().split()))
    numbers.sort(reverse = True)
    print(f'The second largest number is {numbers[1]}')