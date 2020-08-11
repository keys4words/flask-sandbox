# create entries into the tables

from models import db, Puppy, Owner, Toy

tarzan = Puppy('Tarzan')
bobik = Puppy('Bobik')

db.session.add_all([tarzan, bobik])
db.session.commit()

print(Puppy.query.all())
tarzan = Puppy.query.filter_by(name='Tarzan').first()
print(tarzan)

peter = Owner('Peter', tarzan.id)
toy1 = Toy("chew toy", tarzan.id)
toy2 = Toy('Ball', tarzan.id)

db.session.add_all([peter, toy1, toy2])
db.session.commit()

tarzan = Puppy.query.filter_by(name='Tarzan').first()
print(tarzan)

print(tarzan.report_toys())
