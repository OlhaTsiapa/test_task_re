# Task
We have some email addresses in the “username@companyname.com” format, please write a program to print the company name and user name of a given email address in the given format “Company: <company>, user: <username>”. A user should be able to run the program in a terminal with setting command line argument to clear/keep username from digits (by default keep digits in username).
For formatting use f-strings, for parsing use re module.

# Example:
If john123@google.com email address is given as input to the program (without params),
then, the output of the program should be:
Company: google, user: john123

If john123@google.com email address is given as input to the program with param ‘--clear’ or ‘-c’:

Then, the output of the program should be:
Company: google, user: john
