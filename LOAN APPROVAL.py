'''LOAN APPROVAL'''

def loan_approval(age,salary,credit_score):
    if salary>30000 and credit_score>650:
        print('Loan is approved')
    else:
        print('Loan is rejected due to salary or creditscore')
def get_input():
    while True:
        age=int(input('enter your age:'))
        if age<25:
            print("loan is rejected due to restricted age under 25")
        else:
            salary=int(input('enter your current salary:'))
            credit_score=int(input('enter your credit score:'))
            return age,salary,credit_score
def main():
    (age,salary,credit_score)=get_input()
    loan_approval(age,salary,credit_score)
    
main()
