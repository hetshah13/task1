"""A PROBLEM STATEMENT WHERE WE WANT TO VALIDATE GST NUMBER USING REGEX."""
import re

def is_gstin(number):
    pattern = "(?!00)^[0-39]{1}[0-9]{1}[A-Z]{3}[A-CF-PHJLT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}[1-9]{1}[A-Z]{1}\\w$"
    return bool(re.match(pattern,number))

n = input("enter a gst number: ")

if is_gstin(n):
    print(f"{n} is a valid GST Number.")
else:
    print(f"{n} is a not a valid GST Number.")