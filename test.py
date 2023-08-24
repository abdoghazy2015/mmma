from flask import *
import datetime,os,random,string,time
import dataset
from threading import Lock
from functools import wraps
import re
from token_generator import *
#import string
#import random

#def getrand():
#    letters = string.ascii_lowercase
#    return ''.join(random.choice(letters) for i in range(10))

OLD_MINUTES = 30
app = Flask(__name__)
if os.path.isfile("secret_string.txt"):
    with open("secret_string.txt") as key_file:
        app.secret_key = key_file.read()
else:
    app.secret_key = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    open("secret_string.txt","w").write(app.secret_key)

company = "bbbbb"

def exec(input):
	print(input)

print(GetTOK())
