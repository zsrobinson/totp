# totp

> ⚠ Work in progress. Currently, this can only generate codes given a certain secret and time.

A simple python script to generate TOTP codes into the future. Simply follow the prompts after installing the dependencies and running the script.

It may not be possible to view your secret if using a TOTP app such as Google Authenticator. Consider using an app such as [Raivo OTP](https://github.com/raivo-otp/ios-application), which allows you to manage your own TOTP secrets. Plus, it's open source!

### Usage:

```
pip install pyotp dateparser
python totp.py

Welcome to the TOTP generator!
Enter your secret: JBSWY3DPEHPK3PXP
Enter the date: 10/18/22 10:30pm
TOTP at 2022-10-18 22:30:00: 359114
```

*The secret shown above is not a real account, but rather [an example](https://github.com/pyauth/pyotp/blob/develop/README.rst#working-example) from the creators of [pyotp](https://github.com/pyauth/pyotp).*