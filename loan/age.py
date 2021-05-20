# to check the age eligibility of user
# would be calculated as 15%
from complete_registration import age


def less_than_eighteen():
    if age() < 18:
        print("You are ineligible to take a loan")


def eighteen_to_twenty_three():
    if 18 >= age() <= 23:
        print("You are eligible to take the loan of this amount")


def twenty_four_to_twenty_nine():
    if 24 >= age() <= 29:
        print("You are eligible to take the loan of this amount")


def thirty_to_thirty_five():
    if 30 >= age() <= 35:
        print("You are eligible to take the loan of this amount")


def thirty_six_to_thirty_five():
    if 36 >= age() <= 41:
        print("You are eligible to take the loan of this amount")


def forty_two_to_fifty():
    if 42 >= age() <= 50:
        print("You are eligible to take the loan of this amount")


def fifty_one_to_sixty():
    if 51 >= age() <= 60:
        print("You are eligible to take the loan of this amount")


def sixty_one_to_seventy():
    if 61 >= age() <= 70:
        print("You are eligible to take the loan of this amount")


def more_seventy_one():
    if age() > 71:
        print("You are eligible to take the loan of this amount")
