# We have some email addresses in the “username@companyname.com” format, please write a program to print the company name and user name of a given email address in the given format “Company: <company>, user: <username>”. A user should be able to run the program in a terminal with setting command line argument to clear/keep username from digits (by default keep digits in username).
# For formatting use f-strings, for parsing use re module.
#
# Example:
# If john123@google.com email address is given as input to the program (without params),
# then, the output of the program should be:
# Company: google, user: john123
#
# If john123@google.com email address is given as input to the program with param ‘--clear’ or ‘-c’:
#
# Then, the output of the program should be:
# Company: google, user: john

# import argparse
import re
import argparse

parser = argparse.ArgumentParser(description='Test.')
parser.add_argument('--email', type=str)
parser.add_argument('-c', '--clear', action="store_true")

args = parser.parse_args()
email = args.email


# if args.clear:
#     name_user = re.sub(r'\d+', '', user)
#     print("Company: %s, User: %s" % (company, name_user))

if email:
    parsing_email = re.compile(r'(?P<user>[a-z0-9]+)@(?P<company>(?:[a-z0-9]+))')
    result = parsing_email.search(email)
    user = result.group("user")
    company = result.group("company")

    print("Company: %s, User: %s" % (company, user))


# email = input('Input email:')
# parsing_email = re.compile(r'(?P<user>[a-z0-9]+)@(?P<company>(?:[a-z0-9]+))')
# result = parsing_email.search(email)
# user = result.group("user")
# company = result.group("company")
#
# parser = argparse.ArgumentParser()
# parser.add_argument('-c', '--clear', action="store_true")
# parser.add_argument('email', action="store", dest="", type=str)
# args = parser.parse_args()
#
# # if args.clear:
#     name_user = re.sub(r'\d+', '', user)
#     print("Company: %s, User: %s" % (company, name_user))
# # else:
#     print("Company: %s, User: %s" % (company, user))


import argparse
#
# parser = argparse.ArgumentParser(description='Short sample app')
#
# parser.add_argument('-a', action="store_true", default=False)
# parser.add_argument('-b', action="store", dest="b")
# parser.add_argument('-c', action="store", dest="c", type=int)
# #
# print(parser.parse_args(['-a', '-bval', '-c', '3']))
