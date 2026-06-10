acc_no=int(input("enter the last 4 digit of your account no:"))
print("options:")
print("1.check balance")
print("2.Deposit")
print("3.Withdraw")
print("4.Exit")
option=int(input("enter option no:"))
ini_bal=3400
if option==1:
    print("your balance is",ini_bal)
elif option==2:
    print("your balance is",ini_bal)
    deposit=int(input("enter deposit amt:"))
    new_bal=ini_bal+deposit
    print("current balance is",new_bal)
elif option==3:
    print("your balance is",ini_bal)
    withdraw=int(input("enter withdraw amt:"))
    if withdraw>ini_bal:
            print("your balance is less")
    new_bal=ini_bal-withdraw
    print("current balance is",new_bal)
else:
    print("thank you")
