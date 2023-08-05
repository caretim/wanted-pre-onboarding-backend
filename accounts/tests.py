from django.test import TestCase

# Create your tests here.
import bcrypt

password = '1234'.encode('utf-8')
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())


print(hashed_password)