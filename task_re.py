import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument('email', type=str)
parser.add_argument('-c', '--clear', action="store_true")
args = parser.parse_args()


if args.email:
    parsing_email = re.compile(r'(?P<user>[a-z0-9]+)@(?P<company>(?:[a-z0-9]+))')
    result = parsing_email.search(args.email)
    user = result.group("user")
    company = result.group("company")

    if args.clear:
        name_user = re.sub(r'\d+', '', user)
        print("Company: {}, User: {}".format(company, name_user))
    else:
        print("Company: {}, User: {}".format(company, user))
else:
    print("no email")







