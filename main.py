print("Welcome to DiegoBank")

password = 2468

pin = int(input("Enter your PIN: "))

balance = 5000


if pin == password:
    while True:

        print("""
        1) Balance
        2) Withdraw
        3) Deposit Money
        4) Exit
        """)

        try:
            option = int(input("Please choose your trasaction: "))
        except:
            print("Invalid option. Please try again!")

        if option == 1:
            print("Balance: ", totalbalance)

        if option == 2:
            withdraw = int(input("Enter amout to withdraw: "))
            totalbalance = balance - withdraw

            print("The amount been debited from your account")
            print("Your current balance is: ", totalbalance)

        if option == 3:

            deposit = int(input("Enter amount to Deposit: "))
            totalbalance = totalbalance + deposit

            print("The amount has been credited to your account")
            print("Your current balance is: ", totalbalance)

        if option == 4:
            break        
          

else:
    print("Wrong PIN")
    print("Please try again")    