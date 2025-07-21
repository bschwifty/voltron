import pwinput
import string
import time

print("Welcome to Voltron, the password helper-outer.  How strong is your password?")

def help():
    print("Voltron is a command-line utility to analyze the strength of your password.")
    print("Simply type your password in, and Voltron will tell you whether it's a good one or not")

def analysis_len(password):
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

def analysis_charset(password):
    char_score = 0 # can increment with each class of character
    has_lower = int(any(c.islower() for c in password))
    has_upper = int(any(c.isupper() for c in password))
    has_numbers = int(any(c.isdigit() for c in password))
    has_special = int(any(c in string.punctuation for c in password))

    char_score += has_lower
    char_score += has_upper
    char_score += has_numbers
    char_score += has_special
    print(f"Your password uses {char_score} character types.")
    if char_score < 4:
        print("Consider adding more character types to your password.\n")
    else:
        print("Nice job!\n")

def analysis_breach(password, filename='rockyou-top15k.txt'):
    #try:
    with open(filename, 'r', encoding='utf-8') as file:
        passwords = set(line.strip() for line in file)
    
    if password in passwords:
        print("Your password has been exposed in a breach! Please change it to another one.\n")
        return True
    else:
        print("Your password is not in the top 15,000 breached passwords.  Good selection!\n")
        return False

if __name__ == "__main__":
    while True:
        proceed = input("Would you like to check your password now (Y/N)?\n").strip().upper()

        if proceed == "N":
            print("No problem, have a nice day : )")
            exit()

        if proceed == "Y":
            print("\nPlease enter your password. We won't save it, but if you are justifiably paranoid,")
            password = pwinput.pwinput(prompt=' you can put in a similar one for us to analyze instead.\n')
            print(password)  # uncomment for debug only, remove this after testing
            time.sleep(1)
            analysis_len(password)
            time.sleep(1)
            analysis_charset(password)
            time.sleep(1)
            analysis_breach(password)
            time.sleep(1)

            print("\nThanks for using Voltron 💫\n"
            "For more information about good password strategies, you can reference NIST Special \n"
            "Publication 800-63B: https://pages.nist.gov/800-63-3/sp800-63b.html")

            break

        # Error handling for invalidd input:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

# TODO: take a look at NIST 800-63B and maybe reference it in help file
# link to use later: https://pages.nist.gov/800-63-3/sp800-63b.html