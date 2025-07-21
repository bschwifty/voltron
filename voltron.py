import pwinput
import string

"""
- analyze:
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
        print("Your password is between 16 and 25 characters long.  Nice work!  However,")
        print("you may be able to make it longer by using a passphrase.\n")
    else:
        print("Your password is more than 25 characters long.  Good to go!")

def analysis_charset():
    char_score = 0 # can increment with each class of character
    has_lower = int(any(c.islower() for c in password))
    has_upper = int(any(c.isupper() for c in password))
    has_numbers = int(any(c.isdigit() for c in password))
    has_special = int(any(c in string.punctuation for c in password))
    # for debug, delete these before finalizing
    print(has_lower)
    print(has_upper)
    print(has_numbers)
    print(has_special)
    # TODO add cumulative scoring here
    char_score += has_lower
    char_score += has_upper
    char_score += has_numbers
    char_score += has_special
    print(f"Your password uses {char_score} character types.")
    if char_score < 4:
        print("Consider adding more character types to your password.\n")
    else:
        print("Nice job!\n")
    # TODO add print stmts here to effect of "your pw uses x character types"

'''
    'all_letters = password.isalpha()
    if all_letters == True:
        score = 1
    all_numbers = password.isdigit()
    if all_numbers == True:
        score = 1
    if score == 1:
        print("Your password is all one kind of character.  Mix it up a bit for better security.")
'''

while True:
    proceed = input("Would you like to check your password now (Y/N)?\n").strip().upper()

    if proceed == "N":
        print("No problem, have a nice day : )")
        exit()

    if proceed == "Y":
        print("\nPlease enter your password. We won't save it, but if you are justifiably paranoid,")
        password = pwinput.pwinput(prompt=' you can put in a similar one for us to analyze instead.\n')
        print(password)  # uncomment for debug only, remove this after testing
        analysis_len()
        analysis_charset()
        break

    # Error handling for invalidd input:
    print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

# TODO: take a look at NIST 800-63B and maybe reference it in help file
# link to use later: https://pages.nist.gov/800-63-3/sp800-63b.html