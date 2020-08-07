from app import db, Puppy

db.create_all()

sam = Puppy('Sammy', 4)
frank = Puppy('Franky', 1)

print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])
db.session.commit()

print(sam.id)