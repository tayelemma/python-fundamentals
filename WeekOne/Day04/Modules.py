"""
 A module is basically a file containing a set of functions to include in your application. 
 There are core python modules, modules you can install using the pip package manager
 (including Django) as well as custom modules
"""

#core python module
import datetime
from datetime import date

import time
# from time import time

#Pip module
# pip install camelcase 
# pip freeze
from camelcase import CamelCase

# Custom module
from custom_module import validate_email


today = datetime.date.today()
print(today)

day = date.today()
print(day)

timestamp = time.time()
print(timestamp)

# tStamp = time()
# print(tStamp)

c = CamelCase()
print(c.hump('hello there world'))

# Validate email
isValid = validate_email('tom@yahoo.com')
if isValid:
    print(f'This email is valid {isValid}')
