import re

with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()

pattern = re.compile("[A-Z][^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.", re.UNICODE)
findings = re.findall(pattern, book)
print(findings)

