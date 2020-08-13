from flask_bcrypt import Bcrypt


# using bcrypt
bcrypt = Bcrypt()
pass1 = 'supersecretpassword'
hashed_pass = bcrypt.generate_password_hash(pass1)

# print(hashed_pass)
pass2 = 'wefjalsdfj'
# print(bcrypt.check_password_hash(hashed_pass, pass1))

# using Werkzeug
from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash('mypass')
print(hashed_pass)
print(check_password_hash(hashed_pass, 'mypass'))
