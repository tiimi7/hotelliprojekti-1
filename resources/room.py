from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.Room import Room, Reservation

room_list = [] # Tyhjä list huoneille jottei kaikki mene rikki

# Tästä alkaa uuden hotelliprojektin "instruction"
# Tämä oli class InstruvtionListResource, nyt se on RoomListResource

class RoomListResource(Resource):

    def get(self):

        data = []

        for room in room_list:
            if room.is_publish is True:
                data.append(room.data)

        return {'data': data}, HTTPStatus.OK

# Seuraava funktio sovitetaan uuteen Room classiin joka löytyy models/Room.py:sta
# Tällähän voisi päivittää huoneiden tietoja järjestelmään, tosin en tiedä tarvitaanko tätä, vai teemmekö huoneet tietokantaan valmiiksi
# Tulipahan tehtyä
    def post(self):
        data = request.get_json()

        room = Room(id=data['id'],
                        roomSize=data['roomsize'],
                        reservation=data['reservation'],
                        is_free=data['isfree'])


        room_list.append(room)

        return room.data, HTTPStatus.CREATED


class RoomResource(Resource):

    def get(self, room_id):
        room = next((room for room in room_list if room.id == room_id and room.is_publish == True), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        return room.data, HTTPStatus.OK

    def put(self, room_id):
        data = request.get_json()

        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        room.id = data['id']
        room.size= data['size']
        # Tähän voisi koettaa laittaa jotain reservationista, muttei listaan kuten yllö....
        # mahdollinen ratkaisu on vaikka:
        # reservation = True


        return room.data, HTTPStatus.OK

    def delete(self, room_id):
        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        room_list.remove(room)

        return {}, HTTPStatus.NO_CONTENT

# Tätä voisi käyttää varauksen määrittelyyn...
class RoomIsFreehResource(Resource):

    def put(self, room_id):
        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        room.is_free = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, room_id):
        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        room.is_free = False

        return {}, HTTPStatus.NO_CONTENT
