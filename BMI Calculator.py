'''18. BMI Calculator
   - Develop a program to calculate BMI:
     - Input: Weight (kg) and height (m).
     - Output: BMI value and corresponding category (Underweight, Normal, Overweight, Obese).'''

def get_input():
    weight = float(input('Enter weight in KG: '))
    height = float(input('Enter height in meters: '))
    return weight, height

def bmi_calculation(weight, height):
    result = weight / (height ** 2)
    return result

def conclusion(result):
    if result < 18.5:
        print('Underweight')
    elif 18.5 <= result < 24.9:
        print('Normal')
    elif 24.9 <= result < 39.9:
        print('Overweight')
    else:
        print('Obese')
def main():
    weight, height = get_input()
    result = bmi_calculation(weight, height)
    conclusion(result)

main()