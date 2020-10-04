# This is /models/instruction.py designed to meet the needs for practical ex. 2
instruction_list = []

# This function retrieves the last instruction by ID
def get_last_id():

    if instruction_list:

        last_instruction = instruction_list[-1]

    else:

        return 1

    return last_instruction.id + 1
# This is obviously the Instruction class...
# It has the def init -style constructor right at the beginning.
class Instruction:

    def __init__(self, name, description, tools, duration, steps, cost):

        self.id = get_last_id()

        self.name = name

        self.description = description

        self.tools = tools

        self.duration = duration

        self.steps = steps

        self.cost = cost

        self.is_publish = False

# And next we have that Instruction class property that returns data.

    @property
    def data(self):
        return {

            'id': self.id,

            'name': self.name,

            'description': self.description,

            'tools': self.tools,

            'duration': self.duration,

            'steps': self.steps,

            'cost': self.cost

            }
