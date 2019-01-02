from user import User

users = [
User(1,'Jose','mypassword'),
User(2,'Sean','secret')
]

#create a dictionary that is mapping the users to a user name
#for every user in users, grab their user name and then link it to the user object
#{'Jose': <user object>}
#this will allow you to look things up by the username
#username_table['Jose']
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

#THESE FUNCTIONS COME FROM THE DOCUMENTATION FROM FLASK-JWT AND ARE REQUIRED TO MAKE IT WORK
#THEY GET PASSED INTO THE JWT CALL

#Authenticate, takes a user name and an password, check to make sure that the username and password match someone in the database (local storage), return the user if they do exist

def authenticate(username,password):
    #check if user exists and return the user if they do
    #you don't use username_table[username],because if you try to return a key that is not in the dictionary you will get an error
    user = username_table.get(username,None) #will return None if it can't find the user

    if user and password == user.password:
        return user


#Identity

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id,None)
