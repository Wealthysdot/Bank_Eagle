import email
import random

# dictionary
# from admin_investment import *
from admin_investment import *
from email_validation import *

from start import *

database = {
    8651378502: ['Adunni', 'Eagle', 'sobamboadedotun@gmail.com', 'password', 200]
}


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
    is_valid_account_number = accountNumberValidation(account_number_from_user)

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


def accountNumberValidation(account_number):
    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid Account Number, account number should not contain alphabets")
                return False
            except TypeError:
                print("Invalid account type")
                return False

        else:
            print("Please enter a 10 digit account number")
            return False

    else:
        print("Account number is a require field")
        return False


def register():
    print("Please Register your new account")
    # email = validate_email(email)
    first_name = input("Enter first Name \n")
    last_name = input("Enter last Name \n")
    password = input("Create password \n")

    try:
        account_number = generateAccountNumber()
    except ValueError:
        print("Account generation failed due to connection failure")
        init()
    # account number is forming the key and the information(value) is the form
    # the list inside the dictionary
    database[account_number] = [first_name, last_name, email, password, 0]

    print("Your account has been created")
    print("=== ==== === === === ===")
    print("Your account number is: %d" % account_number)
    print("make sure to keep it safe")
    print("=== ==== === === === ===")

    login()


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
        # current_bal = user_details[4]
        # user_details[4] = user_details[4] + deposit
        print("Your current balance is " + str(current_bal))
        return current_bal


def getCurrentBalance(user_detail):
    return "Your current balance is" + str(user_detail[4])


#     return user_detail[4]

# def check_balance(user_detail):
#     balance = balance + user_detail[4]
#     return ("Your current balance is" + balance)
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


# def investment_check():
#     enter = int(input("Do you have an account with BankEagle?\n"
#                       "Press 1 for Yes\n"
#                       "Press 2 for No\n"))
#     if enter == 1:
#         investment()
#     elif enter == 2:
#         print("Please register with BankEagle to access the investment")
#         register()
#         investment()
#     else:
#         print("You have entered an invalid option")


#


def whatToDoNext():
    try:
        proceed = int(input(("Do you want to perform another transaction\n"
                             "Press 1 to continue \n"
                             "Press 2 to exit")))
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
