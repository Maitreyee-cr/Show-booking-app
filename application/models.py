from .database import db
from flask_security import UserMixin
from flask_login import login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=False)
    name=db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    isAdmin = db.Column(db.Boolean())
    #roles = db.relationship('Role', secondary=roles_users,backref=db.backref('users', lazy='dynamic'))
    # venue_manage=db.relationship('Venue',backref='user')
    # show_manage=db.relationship('Show',backref='user')

class Venue(db.Model):
    __tablename__ = 'venue'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    place = db.Column(db.String(255))
    capacity=db.Column(db.Integer)
    # shows=db.relationship('Show',backref='venue',lazy='dynamic')
    user_Id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class show(db.Model):
    __tablename__= 'Show' 
    id = db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(80),unique=True)
    ticket_price=db.Column(db.Integer)
    venue_Id=db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    user_Id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date=db.Column(db.DateTime,nullable=False)
    startTime=db.Column(db.DateTime,nullable=False)
    endTime=db.Column(db.DateTime,nullable=False) # should be calculated with startTime and duration
    # duration=db.Column(db.Integer,nullable=False)
    #bookerId=db.Column(db.Integer, db.ForeignKey('user.id'))
    tags= db.Column(db.String(70))
    
class Review(db.Model):
    __tablename__='rating'
    id = db.Column(db.Integer(),primary_key=True)
    user_Id=db.Column(db.Integer, nullable=False)
    show_Id=db.Column(db.Integer, nullable=False)
    rating=db.Column(db.Integer)
class booking(db.Model):
    __tablename__='Booking'
    id=db.Column(db.Integer(),primary_key=True)
    user_id=db.Column(db.Integer, nullable=False)
    show_id=db.Column(db.Integer, nullable=False)
    count=db.Column(db.Integer())








