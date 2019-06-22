import random
import string
chars = string.ascii_letters + string.digits + '!@#$%^&*'

length = input('password length?: ')
length = int(length)
password = ''
for c in range(length):
    password += random.choice(chars)
print(password + ' is your password.')
