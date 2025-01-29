
#ATM MACHINE
def deposit_money(money_deposit):#MONEY DEPOSIT
     deposit_amount=int(input('enter the amount to deposit:'))
     account_number=int(input('enter the 11 digit account number:'))
     money_deposit+=deposit_amount
     print(f'{ money_deposit } amount credited successfully in account number {account_number}')
     return money_deposit
def money_withdrawl(money_deposit):#MONEY WITHDRWAL
      withdrawl_amount=int(input('enter the amount to be withdrawl:'))
      if withdrawl_amount>money_deposit:
          print('Insufficient amount for withdrawl:')
      else:
       money_deposit-=withdrawl_amount
       print(f'please take your cash:{withdrawl_amount}')
      return money_deposit
def get_input(money_deposit):
    money_deposit=0
    while True:
        choice=int(input('enter your choice: \n 1.check balance\n 2.Deposit Money\n 3.Withdrawl Money\n 4.Exit\n'))
        if choice==1:
            if money_deposit>0:
                print(f'The avialable Balance is {money_deposit}')
            if money_deposit==0:
                print('available Balance is 0 ')
            continue
        if choice==2:
            money_deposit=deposit_money(money_deposit)
        if choice==3:
            money_deposit=money_withdrawl(money_deposit)
        if choice==4:
            print('exited successfully please remove your card')  
        break
def main():
    print('please insert your card')
    pin=int(input('enter your 4 digit pin:'))
    #choice=get_input()
    money_deposit = 0  # Initialize balance as 0
    get_input(money_deposit)
main()


