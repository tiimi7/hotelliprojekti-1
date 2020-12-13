from datetime import datetime
from extensions import db




class Room(db.Model):
    __tablename__ = 'Room'
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    roomSize=db.Column(db.Integer, nullable=True)
#    reservation=db.relationship('Reservation',backref='Room',lazy='dynamic')
    is_free = db.Column(db.Boolean(), default=True)
    is_publish = db.Column(db.Boolean(), default=True)

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def data(self):
        return {
            'id': self.id,
            'roomSize': self.roomSize,
            'isfree': self.is_free,
            'ispublish': self.is_publish,
            'user_id': self.user_id
        }

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_publish=True).all()

    @classmethod
    def get_by_id(cls, room_id):
        return cls.query.filter_by(id=room_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()




class Reservation(db.Model):
    __tablename__ = 'Reservation'
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title=db.Column(db.String(64),nullable=False,unique=True)
#    date=db.Column(db.DateTime,default=datetime.utcnow,nullable=True)
    startTime=db.Column(db.Integer,nullable=True)
    endTime=db.Column(db.Integer,nullable=True)
    duration=db.Column(db.Integer,nullable=True)
    is_publish = db.Column(db.Boolean(), default=False)

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def data(self):
        return {
            'id': self.id,
            'title': self.title,
#            'date': self.date,
            'startTime': self.startTime,
            'endTime': self.endTime,
            'duration': self.duration,
#            'isPublish': self.is_publish,
            'user_id': self.user_id
        }

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_publish=True).all()

    @classmethod
    def get_by_id(cls, room_id):
        return cls.query.filter_by(id=room_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
