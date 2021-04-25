from eagle import *


def message():
    try:
        unit = int(input("The payout type for investment is capital + profit and it would paid on maturity\n"
                         "A unit of the investment is N50 \n"
                         "Please enter the amount of Units you would like to buy: \n"))
    except ValueError:
        print("Please press the correct option for your investment")
    bought_unit = unit * 50
    return bought_unit


def unit_to_buy_in_naira_value():
    for unit, bought_unit in message():
        # try:
        #     bought_unit = unit * 50
        # except ValueError:
        #     print("Please press the correct number of unit for your investment")
        #     unit_to_buy_in_naira_value()

        if bought_unit < getCurrentBalance():
            print("insufficient balance\n"
                  "Please make a deposit into your account to continue")
        else:
            print("You purchased " + bought_unit + "amount of investment\n")


def calc_cassava():
    print(unit_to_buy_in_naira_value())
    calc = ((unit_to_buy_in_naira_value() * 36) / 100) * 18
    investment_return = calc + unit_to_buy_in_naira_value()

    print("You  would receive" + str(investment_return) + "at maturity\n")


def calc_cattle():
    calc = ((unit_to_buy_in_naira_value() * 16) / 100) * 12
    investment_return = calc + unit_to_buy_in_naira_value()
    print("You purchased " + str(message()) + "amount of investment\n"
                                              "You  would receive" + str(investment_return) + "at maturity")


def calc_transport():
    calc = ((unit_to_buy_in_naira_value() * 17) / 100) * 12
    investment_return = calc + unit_to_buy_in_naira_value()

    print("You purchased " + str(message()) + "amount of investment\n"
                                              "You  would receive" + str(investment_return) + "at maturity")


def calc_real_estate():
    calc = ((unit_to_buy_in_naira_value() * 20) / 100) * 6
    investment_return = calc + unit_to_buy_in_naira_value()
    print("You purchased " + str(message()) + "amount of investment\n"
                                              "You would receive" + str(investment_return) + "at maturity\n")


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
