from eagle import *

bought_units = 0


def message():
    try:
        unit = int(input("The payout type for investment is capital + profit and it would paid on maturity\n"
                         "A unit of the investment is N50 \n"
                         "Please enter the amount of Units you would like to buy: \n"))
        global bought_units
        bought_units = unit * 50
    except ValueError:
        print("Please press the correct option for your investment")


def bought_unit():
    global bought_units
    for account_number, user_details in database.items():
        if bought_units > user_details[4]:
            print("insufficient balance\n"
                  "Please make a deposit into your account to continue")
        else:
            print("You purchased " + str(bought_units) + "worth of investment\n")


def calc_cassava():
    message()
    bought_unit()
    global bought_units
    calc = ((bought_units * 36) / 100) * 18
    investment_return = calc + bought_units
    print("You  would receive " + str(investment_return) + " at maturity\n")
    whatToDoNext()


def calc_cattle():
    message()
    bought_unit()
    global bought_units
    calc = ((bought_units * 16) / 100) * 12
    investment_return = calc + bought_units
    print("You  would receive" + str(investment_return) + "at maturity\n")


def calc_transport():
    message()
    bought_unit()
    global bought_units
    calc = ((bought_units * 17) / 100) * 12
    investment_return = calc + bought_units

    print("You  would receive" + str(investment_return) + "at maturity")
    whatToDoNext()


def calc_real_estate():
    message()
    bought_unit()
    global bought_units
    calc = ((bought_units * 20) / 100) * 6
    investment_return = calc + bought_units
    print("You would receive" + str(investment_return) + "at maturity\n")
    whatToDoNext()

# def cryptocurrency():
#     message()
#     bought_unit()
#     global bought_units
#     calc = (bought_units * )


def investment():
    try:
        investment_list = int(input("Press 1 for Cassava farm(36% returns in 18months) \n"
                                    "Press 2 for cattle rearing farm (16% returns in 12months) \n"
                                    "Press 3 for Transport (17% returns in 17months) \n"
                                    "Press 4 for Real Estate (28% returns in 17months) \n"))
    except ValueError:
        return "Please press the correct option for your investment"

    if investment_list == 1:
        calc_cassava()

    elif investment_list == 2:
        calc_cattle()

    elif investment_list == 3:
        calc_transport()

    elif investment_list == 4:
        calc_real_estate()

    else:
        print("Invalid option selected")
        investment()
        whatToDoNext()

