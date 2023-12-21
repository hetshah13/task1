"""A PROBLEM STATEMENT WHERE WE WANT TO VALIDATE PANCARD NUMBER USING REGEX."""
import re 

def valid(number):
    pattern = "^[A-Z]{3}[A-CF-PHJLT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]$"
    return bool(re.match(pattern,number))

n = input("enter your number: ")

if valid(n):
    print(f"{n} is a valid pan number.")
else:
    print(f"{n} is a invalid pan number.")
