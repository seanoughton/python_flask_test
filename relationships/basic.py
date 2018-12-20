#CREATE ENTRIES INTO THE TABLES

from models import db,Puppy,Owner,Toy

#Create 2 puppies

rufus = Puppy('Rufus')
fido = Puppy('Fido')

#Add puppies to the DATABASE
db.session.add_all([rufus,fido])
db.session.commit

#check
print(Puppy.query.all())


rufus = Puppy.query.filter_by(name='Rufus').first()


#create an owner

jose = Owner('Jose',rufus.id)
print(rufus.owner)

#give rufus some toys

toy1 = Toy('ChewToy',rufus.id)
toy2 = Toy('Ball',rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit


#grab rufus after the additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
print(rufus.report_toys())
