import string
from random import choice
import random

from random import choice
#List of first names

first_names=['Jon','Rick','Ben','Vishal']

#List of last names

last_names=['Johnson','Andrews','Smith','Williams']
first, last=choice(first_names), choice(last_names)

##email address
#-----------------------
#valid email service: gmail, hotmail,yahoo, outlook, icloud

email_servics=['gmail.com','hostmail.com','yahoo.com','outlook.com','icloud.com']

###random phone number format
#--------------------------------
#978-356-6754
for i in range(100):
    print('-------------------------------------------------------')
    random_name='{} {}'.format(choice(first_names),choice(last_names))
    ''.format()
    print(random_name)
    random_email_service = choice(email_servics)
    print('Email address: {}@{}'.format(random_name, random_email_service))
    print('phone number:')
    random_phone_number1 = random.randint(101, 999)
    random_phone_number2 = random.randint(101, 999)
    random_phone_number3 = random.randint(1001, 9999)
    print('{}-{}-{}'.format(random_phone_number1,random_phone_number2,random_phone_number3))

