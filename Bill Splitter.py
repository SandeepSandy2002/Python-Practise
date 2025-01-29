'''10. Bill Splitter
   - Create a program to split a bill among a group of people:
     - Input: Total bill amount, number of people, and any tip percentage.
     - Output: Amount each person has to pay.'''

def bill_splitter(totalbill,tip,people):#BILL SPLITTER
    money=((totalbill+tip)/people)
    return money
def tip_money(totalbill,tips):#TIP COLLECTION
    tip=(totalbill*(tips/100))
    return tip
def get_input():#GET INPUTS
    totalbill=float(input('enter the total bill:'))
    tips=int(input('enter the tip in percentage(%):'))
    people=int(input('enter the number of people:'))
    return totalbill,tips,people
def main():#MAIN FUNCTION AND PRINT VALUES
    (totalbill,tips,people)=get_input()
    tip=tip_money(totalbill,tips)
    bill=bill_splitter(totalbill,tip,people)
    print(f'Each person needs to pay:{bill}')
main()