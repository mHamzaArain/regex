#! python3

import re, pyperclip

# TODO: Create a regex for phone number
phoneRegex = re.compile(r'''

# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?            # area code (optional)
(\s|-)            # first separator
\d\d\d            # first 3 digits
-            # separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)    # extension word-part (optional)
(\d{2,5}))?          # extension number-part(optional)
)

''', re.VERBOSE)
# TODO: Create Regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5})?.com
# General Email Regex (RFC 5322 Official Standard)
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*
|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|
\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+
[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|
[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|
[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|
\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
''', re.VERBOSE)
# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone form this text
extractedPhone = phoneRegex.findall(text) 
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedEmail)
# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)