from extensions import db
# This is /models/instruction.py designed to meet the needs for practical ex. 2
instruction_list = []

# This function retrieves the last instruction by ID
def get_last_id():

    if instruction_list:

        last_instruction = instruction_list[-1]

    else:

        return 1

    return last_instruction.id + 1


# This is the database model for SQLAlchemy, it has variables for all the columns we need


class Instruction(db.Model):

    __tablename__ = 'instruction'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    tools = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    steps = db.Column(db.String(1000))
    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))