import pyotp
import dateparser
import warnings

print("")
print("Welcome to the TOTP generator!")

# Ask user for secret

secret = input("Enter your secret: ")
totp = pyotp.TOTP(secret)

# Don't print warning about dateparser not needing to run the localize method

warnings.filterwarnings(
    "ignore",
    message="The localize method is no longer necessary, as this time zone supports the fold attribute",
)

# Ask user for date

date_input = input("Enter the date: ")
date = dateparser.parse(date_input)

# Generate TOTP

print(f"TOTP at {date}: {totp.at(date)}")
