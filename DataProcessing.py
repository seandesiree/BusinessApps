import re

try:
    with open('contacts.txt', "r") as file:
        content = file.read()
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}", content)
        print(emails)
except FileNotFoundError:
    []

