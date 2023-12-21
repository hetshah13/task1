"""A PROBLEM STATMENT WHERE VALIDATION OF AADHAR CARD NUMBER"""
import re
def is_aadhar(number):
    pattern = "^[2-9]{1}[0-9]{3}\\s(?!0000)(?!0100)[0-9]{4}\\s(?!0000)(?!1000)[0-9]{4}$"
    return bool(re.match(pattern,number))

n = input("enter a aadhar number: ")

if is_aadhar(n):
    print(f"{n} is a valid aadhar number.")
else:
    print(f"{n} is a not a valid aadhar number.")