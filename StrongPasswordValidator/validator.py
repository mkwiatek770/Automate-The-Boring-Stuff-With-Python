import re

validators = {
    "At least one big letter": re.compile(r"[A-Z]"),
    "At least one small letter": re.compile(r"[a-z]"),
    "At least one number letter": re.compile(r"[0-9]"),
    "Length greater or equal than 8 characters": re.compile(r".{8,}")
}
user_password = input("Type Password, we'll tell you if it's strong: ")

errors = []
for message, regex in validators.items():
    if not regex.search(user_password):
        errors.append(message)

if not errors:
    print("Password is strong")
else:
    print("Password is weak, errors:\n{}".format("\n".join(errors)))
