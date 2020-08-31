import onetimepass as otp
my_secret = 'MFRGGZDFMZTWQ2LK'
my_token = otp.get_totp(my_secret)
print(my_token)