import pwinput
import string

"""
- measure:
    - charset
    - check against breach database..? maybe shortened version of rockyou, top 100k or such?
"""
print("Welcome to Voltron, the password helper-outer.  How strong is your password?")

def help():
    print("Voltron is a command-line utility to analyze the strength of your password.")
    print("Simply type your password in, and Voltron will tell you whether it's a good one or not")

def analysis_len():
    # XKCD check:
    if password == "correcthorsebatterystaple":
        print("That's an excellent password, but everyone else has read XKCD too...\n")
        exit()
    # Length checks:
    if len(password) < 16:
        print("Your password is shorter than 16 characters long, consider making it longer.")
    elif len(password) >= 16 and len(password) < 25:
        print("Your password is between 16 and 25 characters long.  Nice work!  However,\n")
        print("you may be able to make it longer by using a passphrase.")
    else:
        print("Your password is more than 25 characters long.  Good to go!")

def analysis_charset():
    #TODO charset analysis goes here - try using isalpha() from string
    # https://www.geeksforgeeks.org/python-string-isalpha-method/?ref=ml_lbp
    # https://pythonskills.org/topics/string-character-analysis
    pass

proceed = input("Would you like to check your password now (Y/N)?\n").strip().upper()

if proceed == "N":
    print("No problem, have a nice day : )")
    exit()

if proceed == "Y":
    print("\nPlease enter your password.  We won't save it, but if you are justifiably paranoid,")
    password = pwinput.pwinput(prompt=' you can put in a similar one for us to analyze instead.\n')
    print(password) # uncomment for debug only, remove this after testing
    analysis_len()
