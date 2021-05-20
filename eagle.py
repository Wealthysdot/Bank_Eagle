import email
import random
import validation

# dictionary
# from admin_investment import *
from admin_investment import *
import database

from start import *


def init():
    print("Welcome to bank Eagle")
    try:
        have_account = int(input("Do you have an account: Enter 1(Yes) or 2(NO) \n"))
    except ValueError:
        print("Please enter the correspondent number for your transaction")
        init()

    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("=== ==== === Login === === ===")

    account_number_from_user = input("Enter account number \n")
    is_valid_account_number = validation.accountNumberValidation(account_number_from_user)

    if is_valid_account_number:
        password = input("Enter password \n")

        for account_number, user_details in database.items():
            if account_number == int(account_number_from_user):
                if user_details[3] == password:
                    bankOperation(user_details)
        print('Invalid account or password')
        login()
    else:
        init()


def register():
    print("Please Register your new account")
    first_name = input("Enter first Name \n")
    last_name = input("Enter last Name \n")
    mail = input("Enter e-mail \n")
    password = input("Create password \n")

    account_number = generateAccountNumber()

    is_user_created = database.create(account_number, [first_name, last_name, mail, password, 0])
    # use database module to create a new user record

    if is_user_created:

        print("Your account has been created")
        print("=== ==== === === === ===")
        print("Your account number is: %d" % account_number)
        print("make sure to keep it safe")
        print("=== ==== === === === ===")

        login()
    else:
        print("Please try again")
        register()


def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    try:
        selected_option = int(input("Press 1 to make a deposit \n"
                                    "Press 2  to make withdrawals \n"
                                    "Press 3 to make investments\n"
                                    "Press 4 to Logout\n"
                                    "Press 5 to Exit\n"))
    except ValueError:
        print("Please the correct option for your transaction")
        return

    if selected_option == 1:
        depositOperation()
    elif selected_option == 2:
        withdrawalOperation()
    elif selected_option == 3:
        investment()
    elif selected_option == 4:
        logout()
    elif selected_option == 5:
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)


def setCurrentBalance(deposit):
    for account_number, user_details in database.items():
        current_bal = user_details[4] + deposit
        print("Your current balance is " + str(current_bal))
        return current_bal


def getCurrentBalance(user_detail):
    return "Your current balance is" + str(user_detail[4])


def withdrawal(amount):
    for account_number, user_details in database.items():
        user_details[4] = user_details[4] - amount
    return user_details[4]


def withdrawalOperation():
    for account_number, user_details in database.items():
        try:
            withdraw = int(input('How much do you want to withdraw\n'))
        except ValueError:
            print("Please input amount to withdraw in digit\n")
            withdrawalOperation()
        if withdraw > user_details[4]:
            print("Insufficient funds")
        else:
            print("Please take your cash")
            print("your current balance is " + str(withdrawal(withdraw)))
    whatToDoNext()


def depositOperation():
    for account_number, user_details in database.items():

        try:
            deposit = int(input('How much do you want to deposit? \n'))
        except ValueError:
            print("Please input amount to deposit in digit \n")

        print(setCurrentBalance(deposit))
        print("You have just deposited, " + str(deposit))

    whatToDoNext()


def whatToDoNext():
    try:
        proceed = int(input(("Do you want to perform another transaction\n"
                             "Press 1 to continue \n"
                             "Press 2 to exit \n")))
    except ValueError:
        print("Please input the ")

    if proceed == 1:
        for account_number, user_details in database.items():
            bankOperation(user_details)
    elif proceed == 2:
        exit()

    else:
        print("Invalid option entered")
        whatToDoNext()


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


def logout():
    login()


if __name__ == '__main__':
    init()
