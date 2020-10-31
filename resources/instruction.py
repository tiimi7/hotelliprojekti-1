from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.instruction import Instruction, instruction_list

# This is the resources/instruction.py for web app. It is kinda similiar from the earlier projects, so I kinda reused it
# Works fine as always.
class InstructionListResource(Resource):

    def get(self):

        data = []

        for instruction in instruction_list:
            if instruction.is_publish is True:
                data.append(instruction.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        instruction = Instruction(name=data['name'],
                        description=data['description'],
                        tools=data['num_of_tools'],
                        duration=data['work_time'],
                        steps=data['directions'])

        instruction_list.append(instruction)

        return instruction.data, HTTPStatus.CREATED


class InstructionResource(Resource):

    def get(self, instruction_id):
        instruction = next((instruction for instruction in instruction_list if instruction.id == instruction_id and instruction.is_publish == True), None)

        if instruction is None:
            return {'message': 'instruction not found'}, HTTPStatus.NOT_FOUND

        return instruction.data, HTTPStatus.OK

    def put(self, instruction_id):
        data = request.get_json()

        instruction = next((instruction for instruction in instruction_list if instruction.id == instruction_id), None)

        if instruction is None:
            return {'message': 'instruction not found'}, HTTPStatus.NOT_FOUND

        instruction.name = data['name']
        instruction.description = data['description']
        instruction.tools = data['tools']
        instruction.duration = data['duration']
        instruction.steps = data['steps']

        return instruction.data, HTTPStatus.OK

    def delete(self, instruction_id):
        instruction = next((instruction for instruction in instruction_list if instruction.id == instruction_id), None)

        if instruction is None:
            return {'message': 'instruction not found'}, HTTPStatus.NOT_FOUND

        instruction_list.remove(instruction)

        return {}, HTTPStatus.NO_CONTENT


class InstructionPublishResource(Resource):

    def put(self, instruction_id):
        instruction = next((instruction for instruction in instruction_list if instruction.id == instruction_id), None)

        if instruction is None:
            return {'message': 'instruction not found'}, HTTPStatus.NOT_FOUND

        instruction.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, instruction_id):
        instruction = next((instruction for instruction in instruction_list if instruction.id == instruction_id), None)

        if instruction is None:
            return {'message': 'instruction not found'}, HTTPStatus.NOT_FOUND

        instruction.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
