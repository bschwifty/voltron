"""
Psuedocode/brainstorming:
- give user an intro blurb
- take current pw
- measure:
    - length
    - charset
    - check against breach database..? maybe shortened version of rockyou, top 100k or such?
"""


print("Welcome to Voltron, the password analyzer.  How strong is your password?")
print("Please enter your password.  We won't save it, but if you are justifiably paranoid,")
password = input(" you can put in a similar one for us to analyze instead.\n")
print(password)

def help():
    pass