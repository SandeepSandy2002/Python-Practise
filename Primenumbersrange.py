import math
#def display(a,b,data):
    
def get_input():#GETTING INPUTS
    while True:
        a = int(input('Enter the starting number: '))
        if a < 0:
            print('Please enter a positive number for the starting number.')
            continue  # Skip to the next iteration if input is invalid
        b = int(input('Enter the ending number: '))
        if a >= b:
            print('Starting number must be smaller than the ending number.')
        else:
            return a, b
def is_prime(n):#CHECKING FOR PRIME
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
         return False
    return True
def prime_numbers(a,b): #BY USING ARRAYS TO STORE THE VALUES
    print(f'the prime numbers in between{a} and {b} is:')
    for i in range(a,b+1):
        if is_prime(i):
           print(i)
    
def main():#MAIN FUNCION
    a,b=get_input()
    prime = prime_numbers(a,b)
    #display(a,b,prime)
main()
