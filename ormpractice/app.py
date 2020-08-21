from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///webinar.db', echo=True)
base = declarative_base()

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return f"<User {self.name} {self.fullname}>"

# create base
# base.metadata.create_all(engine)

# create
session = sessionmaker(bind=engine)()
# user_ivan = User(name='Ivan', fullname='Ivan Ivanov')
# session.add(user_ivan)
# session.commit()

# read
# q = session.query(User).filter_by(name='Ivan').first()
s = session.execute("select * from users")
d, a = {}, []
for rowproxy in s:
    # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
    for column, value in rowproxy.items():
        # build up the dictionary
        d = {**d, **{column: value}}
    a.append(d)

print(a)

# bulk create
# session.add_all([User(name='Peter', fullname='Penn'), User(name='Mike', fullname='Tyson')])
# session.commit()
