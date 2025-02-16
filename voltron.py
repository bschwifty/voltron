import math

"""
Psuedocode/brainstorming:
- give user an intro blurb
- take current pw
- measure:
    - length
    - charset
    - check against breach database..? maybe shortened version of rockyou, top 100k or such?
"""


print("Welcome to Voltron, the password helper-outer.  How strong is your password?")

proceed = input("Would you like to check your password now (Y/N)?\n").strip().upper()

if proceed == "N":
    print("No problem, have a nice day.")
    exit()

if proceed == "Y":
    analysis()

print("Please enter your password.  We won't save it, but if you are justifiably paranoid,")
password = input(" you can put in a similar one for us to analyze instead.\n")
print(password)

def help():
    print("Voltron is a command-line utility to analyze the strength of your password.")
    print("Simply type your password in, and Voltron will tell you whether it's a good one or not")

def analysis():
    print("TODO: analysis goes here")
    pass