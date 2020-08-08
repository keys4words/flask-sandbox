from app import db, Puppy

# create
my_puppy = Puppy('Buska', 4)
db.session.add(my_puppy)
db.session.commit()

# read
all_puppies = Puppy.query.all()
print(all_puppies)

# select by id
puppy_one = Puppy.query.get(1)
print(puppy_one)

# fitler
puppy_franky = Puppy.query.filter_by(name='Franky')
print(puppy_franky.all())

# update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
