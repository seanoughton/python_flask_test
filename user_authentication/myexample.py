# from flask_bcrypt import Bcrypt
#
# #Create an instance of the hashing object
# bcrypt = Bcrypt()
#
# password = 'mypassword'
#
# hashed_password = bcrypt.generate_password_hash(password)
#
# # print (hashed_password)
#
# #Checking the password hash
# check = bcrypt.check_password_hash(hashed_password,'wrongpassword')
# print(check)

from werkzeug.security import generate_password_hash,check_password_hash

hashed_pass = generate_password_hash('mypassword')
print(hashed_pass)

check = check_password_hash(hashed_pass,'wrongpassword')
print(check)
