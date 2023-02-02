import re

def emverify(em):
    regex = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.search(regex,em)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")
while True:
    print(emverify(input('Email:>')))