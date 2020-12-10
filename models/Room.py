from datetime import datetime
from extensions import db




class Room(db.Model):
    __tablename__ = 'Room'
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    roomSize=db.Column(db.Integer, nullable=False)
    reservation=db.relationship('Reservation',backref='Room',lazy='dynamic')
    is_free = db.Column(db.Boolean(), default=False)

class Reservation(db.Model):
    __tablename__ = 'Reservation'
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title=db.Column(db.String(64),nullable=False,unique=True)
    date=db.Column(db.DateTime,nullable=False)
    startTime=db.Column(db.Integer,nullable=False)
    endTime=db.Column(db.Integer,nullable=False)
    duration=db.Column(db.Integer,nullable=False)