# import re
# from email_validator import validate_email, EmailNotValidError
#
# email = "my+address@mydomain.tld"
#
#
# # regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
#
#
# def validate_email(email):
#     input("Enter e-mail address \n")
#     # if re.search(regex, email):
#     #     print("Valid Email")
#     # else:
#     #     print("Invalid Email")
#
#     try:
#         # Validate.
#         valid = validate_email(email)
#
#         # Update with the normalized form.
#         email = valid.email
#     except EmailNotValidError as e:
#         # email is not valid, exception message is human-readable
#         print(str(e))
#
#
# if __name__ == '__main__':
#     validate_email(email)
