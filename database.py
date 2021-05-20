# CRUD
# create record
# update record
# read record
# delete record

# find user

import os

user_db_path = "data/user_record/"


def create(account_number, user_details):
    completion_state = False

    try:

        f = open(user_db_path + str(account_number) + ".txt", "x")

    except FileExistsError:

        print("User already exist")
        # delete the already created file, and print out error, then return false
        # check content of file before deleting
        # delete(account_number)
    else:

        f.write(str(user_details))
        completion_state = True

    finally:

        f.close()
        return completion_state

    # create a file - account_number.xt
    # add user details to file
    # return true
    # if savings to file fails, then delete created file


def read(user_account_number):
    print("read user record")
    #     find user with account number
    # fetch content of file


def update(user_account_number):
    print("update user record")
    # find user with account number
    # fetch and update content of file
    # save file back into data folder
    # return true


def delete(user_account_number):
    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:
            return is_delete_successful
    # find user with account number
    # delete user record(file)
    # return true


def find(user_account_number):
    print("find user")


# find user record in the data folder
    print(delete(5523710759))
