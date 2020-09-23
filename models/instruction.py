instruction_list = []

def get_last_id():

    if instruction_list:

        last_instruction = instruction_list[-1]

    else:

        return 1

    return last_instruction.id + 1

class Instruction:

    def __init__(self, name, description, num_of_tools, work_time, directions):

        self.id = get_last_id()

        self.name = name

        self.description = description

        self.num_of_tools = num_of_servings

        self.work_time = cook_time

        self.directions = directions

        self.is_publish = True

        @property
        def data(self):
            return {

                'id': self.id,

                'name': self.name,

                'description': self.description,

                'num_of_tools': self.num_of_tools,

                'work_time': self.work_time,

                'directions': self.directions

            }
