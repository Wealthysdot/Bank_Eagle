# complete registration(KYC)by entering:
# age
# employment status
# next of kin
# address
# BVN
# NIN

# would be used when customer needs other services, such as loan and investment
# or after they have made about 5 transaction and, they would then be forced to
# complete the registration to continue the platform and make their transaction safe
def process_of_complete_registration():
    employ_stat()
    age()
    address()
    BVN()
    n_of_kin()



def employ_stat():
    print("What your employment status")

    try:
        selected_option = int(input("Press 1 for Student \n"
                                    "Press 2 for Employed \n"
                                    "Press 3 for Self-Employed\n"
                                    "Press 4 for Unemployed\n"
                                    "Press 5 for Retired\n"))
    except ValueError:
        print("Please the correct option for your transaction")
        return

    if selected_option == 1:
        print("student")
    elif selected_option == 2:
        print("Employed")
    elif selected_option == 3:
        print("self-employed")
    elif selected_option == 4:
        print("unemployed")
    elif selected_option == 5:
        print("retired")
    else:
        print("Invalid option selected")
        employ_stat()


def age():
    int(input("How old are you?"))


def address():
    input("Please enter your home address")


def BVN():
    int(input("Please enter your BVN"))


def NIN():
    int(input("Please enter your NIN"))


def n_of_kin():
    name = input("Name of next of kin")
    phone = int(input("Phone number of next of kin"))
    addy = input("Address of next of kin")


process_of_complete_registration()
