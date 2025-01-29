'''16. Odd and Even Separator
   - Write a program that takes a list of numbers as input and separates them into odd and even lists.'''

def get_input():
    numbers = list(map(int, input('enter the numbers:').split()))
    even = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
            even.sort()
        else:
            odd.append(number)
            odd.sort()
    return even, odd

def main():
    even, odd = get_input()
    print(f'The even number  list is {even}')
    print(f'The odd number list is {odd}')

main()