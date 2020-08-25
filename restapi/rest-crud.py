from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'verysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'puppies.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
api = Api(app)
jwt = JWT(app, authenticate, identity)


class Puppy(db.Model):
    name = db.Column(db.String(80), primary_key=True)

    def json(self):
        return {'name': self.name}


# {'name': 'Bobik'}
# puppies = []

class PuppyNames(Resource):

    def get(self, name):
        # for pup in puppies:
        #     if pup['name'] == name:
        #         return pup
        # return {'name': None}, 404
        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            return pup.json()
        else:
            return {'name': None}, 404

    def post(self, name):
        # pup = {'name': name}
        # puppies.append(pup)
        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()

        return pup.json()

    def delete(self, name):
        # for i, pup in enumerate(puppies):
        #     if pup['name'] == name:
        #         deleted_pup = puppies.pop(i)
        #         return {'note': 'delete success'}
        pup = Puppy.query.filter_by(name=name).first()
        db.session.delete(pup)
        db.session.commit()
        return {'note': 'delete success'}


class AllNames(Resource):
    # @jwt_required()
    def get(self):
        # return {'puppies': puppies}
        puppies = Puppy.query.all()
        return [pup.json() for pup in puppies]


api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')

if __name__ == "__main__":
    app.run(debug=True)