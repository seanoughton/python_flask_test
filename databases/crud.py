from basic import db,Puppy


## CREATE
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

## READ
all_puppies = Puppy.query.all() #returns a list of the puppy objects in the table
print(all_puppies)

# Select by Id
puppy_one = Puppy.query.get(1)

#filter by an attribute
puppy_frankie = Puppy.query.filter_by(name="Frankie")
puppy_frankie.all() #gives you a list of all the puppies returned from the db

## UPDATE
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

## DELETE
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
