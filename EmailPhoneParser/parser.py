"""
Program that fetches text from clipboard, takes all phone number patterns and
email patterns and return these patterns
"""
import re
import pyperclip

phone_regex = re.compile(r"((\+48)\s)?\b(\d{3}-\d{3}-\d{3}|(\d{9})|(\d{3}\s\d{3}\s\d{3}))\b")
email_regex = re.compile(r"\b[a-zA-Z0-9_.-]+@[a-zA-Z0-9]+\.[a-z]+\b")


def text_from_clipboard():
    return pyperclip.paste()


def all_phone_numbers(text):
    return phone_regex.findall(text)


def all_emails(text):
    return email_regex.findall(text)


def main():
    text = text_from_clipboard()
    phone_numbers = all_phone_numbers(text)
    emails = all_emails(text)

    if emails:
        print("Emails:")
        for i, email in enumerate(emails, 1):
            print("{}.   {}".format(i, email))
    else:
        print("No emails found")

    if phone_numbers:
        print("Phone Numbers:")
        for i, number in enumerate(phone_numbers, 1):
            num = "{} {}".format(number[1], number[2]).strip()
            print("{}.   {}".format(i, num))
    else:
        print("No numbers found")


if __name__ == "__main__":
    main()
