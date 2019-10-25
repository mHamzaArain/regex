#!/usr/bin/python3

"""Program to Detect Wheter a Password is Strong or Not."""

import re
import pyperclip


# Function to check the above regexes
def password_strength_checker(password):
    """Using a regex in Python, how can I verify that a user's password is:

    At least 8 characters
    Must be restricted to, though does not specifically require any of:
    *    uppercase letters: A-Z
    *    lowercase letters: a-z
    *    numbers: 0-9
    *    any of the special characters: @#$%^&+=
    """
    if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return True     # matched
    else:
        return False    # no match

# Retrieve Password from clipboard
password_retrive = str(pyperclip.paste())

# Run it through the function and print relevant message to the console
if password_strength_checker(password_retrive) is True:
    print('That\'s a strong password. Remember to use it for one site only.')
else:
    print('That\'s a weak password. I wouldn\'t recommend using it')
