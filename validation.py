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

# def validate_registration_input(input):
# def email_validation():
