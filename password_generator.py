import random
import string

print('''
    
 /$$$$$$$$                                        
|_____ $$                                         
     /$$/   /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$ 
    /$$/   /$$__  $$| $$  | $$ /$$__  $$ /$$__  $$
   /$$/   | $$$$$$$$| $$  | $$| $$  \ $$| $$$$$$$$
  /$$/    | $$_____/| $$  | $$| $$  | $$| $$_____/
 /$$$$$$$$|  $$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$
|________/ \_______/ \______/  \____  $$ \_______/
                               /$$  \ $$          
                              |  $$$$$$/          
                               \______/    
    ''')
chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-=`]}['

length = input('password length?: ')
length = int(length)

password = ''

for c in range(length):

    password += random.choice(chars)

print(password + ' is your password.')
