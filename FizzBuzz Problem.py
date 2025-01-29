
'''20. FizzBuzz Problem
   - Write a program that prints numbers from 1 to 100, but:
     - Prints "Fizz" for multiples of 3.
     - Prints "Buzz" for multiples of 5.
     - Prints "FizzBuzz" for multiples of both 3 and 5.'''

def multiples_3(n):
    if n%3==0:
        return("Fizz")
def multiples_5(n):
    if n%5==0:
        return('Buzz')
def multiples_3and5(n):
    if n%3==0 and n%5==0:
        return 'FizzBuzz'
def main():
    for i in range(1,101):
        output=multiples_3and5(i)
        if not output:
            output=multiples_3(i) or multiples_5(i)
    
        if output:
            print(output)
        else:
            print(i)