from basic import db,Puppy #imports the databse and the puppy class

#CREATES ALL OF THE TABLES from the Models
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankei',4)

print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])

db.session.commit() #saves changes to the database

print(sam.id)
print(frank.id)
