from extensions import db
# This is /models/reservation.py designed to meet the needs for practical ex. 2
reservation_list = []


# This function retrieves the last reservation by ID
def get_last_id():

    if reservation_list:

        last_reservation = reservation_list[-1]

    else:

        return 1

    return last_reservation.id + 1


# This is the database model for SQLAlchemy, it has variables for all the columns we need


class Reservation(db.Model):

    __tablename__ = 'reservation'

    #Varauksen mallin määritys
    id = db.Column(db.Integer, primary_key=True)
    room_size = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    reservation_start = db.Column(db.Integer, primary_key=True)
    reservation_end = db.Column(db.Integer, primary_key=True)

    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
