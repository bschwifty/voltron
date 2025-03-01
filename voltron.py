import math
import pwinput

"""
- measure:
    - length
    - charset
    - check against breach database..? maybe shortened version of rockyou, top 100k or such?
"""
print("Welcome to Voltron, the password helper-outer.  How strong is your password?")

def help():
    print("Voltron is a command-line utility to analyze the strength of your password.")
    print("Simply type your password in, and Voltron will tell you whether it's a good one or not")

def analysis():
    print("Please enter your password.  We won't save it, but if you are justifiably paranoid,")
    password = pwinput.pwinput(prompt=' you can put in a similar one for us to analyze instead.\n')
    print(password) # debug only, remove this after testing
    if len(password) < 16:
        print("Your password is shorter than 16 characters long, consider making it longer.")
    elif len(password) >= 16 and len(password) < 25:
        print("Your password is between 16 and 25 characters long.  Nice work!  However,\n")
        print("you may be able to make it longer by using a passphrase.")

proceed = input("Would you like to check your password now (Y/N)?\n").strip().upper()

if proceed == "N":
    print("No problem, have a nice day.  : )")
    exit()

if proceed == "Y":
    analysis()

