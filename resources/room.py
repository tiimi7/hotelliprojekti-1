from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional
from http import HTTPStatus

from models.Room import Room, Reservation

# Tässä tiedostossa on aluksi models.py:n Room Classille resourcet,
# niiden jälkeen models.py:n Reservationin resourcet.


class RoomListResource(Resource):

    def get(self):

        rooms = Room.get_all_published()

        data = []

        for room in rooms:
            data.append(room.data())

        return {'data': data}, HTTPStatus.OK

    @jwt_required
    def post(self):
        json_data = request.get_json()

        current_user = get_jwt_identity()

        room = Room(roomSize=json_data['roomSize'],
#                        reservation=json_data['reservation'],
#                        is_free=json_data['isfree'], # tuskin booleania voi tällä tavoin muuttaa, jos ei toimi, kokeile ['is_free = True']
#                        is_publish=json_data['ispublish'], # Sana kuin yllä
                        user_id=current_user)

        room.save()

        return room.data(), HTTPStatus.CREATED


class RoomResource(Resource):

    @jwt_optional
    def get(self, room_id):

        room = Room.get_by_id(room_id=room_id)

        if room is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if room.is_publish == False and room.user_id != current_user:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        return room.data(), HTTPStatus.OK

    @jwt_required
    def put(self, room_id):

        json_data = request.get_json()

        room = Room.get_by_id(room_id=room_id)

        if room is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != room.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        Room.id = json_data['id']
        Room.roomSize = json_data['roomSize']
#        Room.reservation = json_data['reservation']
#        Room.is_free = json_data['isfree'] # Nämä eivät varmaankaan toimi ihan nöin
        Room.is_publish = json_data['isfree']

        Room.save()

        return room.data(), HTTPStatus.OK

    @jwt_required
    def delete(self, room_id):

        room = Room.get_by_id(room_id=room_id)

        if room is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != room.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        room.delete()

        return {}, HTTPStatus.NO_CONTENT


class RoomPublishResource(Resource):

    @jwt_required
    def put(self, room_id):
        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != room.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        room.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    @jwt_required
    def delete(self, room_id):
        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != room.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        room.is_publish = False

        return {}, HTTPStatus.NO_CONTENT

class RoomIsFreeResource(Resource):

    @jwt_required
    def put(self, room_id):
        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != room.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        room.is_free = True

        return {}, HTTPStatus.NO_CONTENT

    @jwt_required
    def delete(self, room_id):
        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != room.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        room.is_free = False

        return {}, HTTPStatus.NO_CONTENT


# Reservationin resourcet alkavat tästä

class ReservationListResource(Resource):

    def get(self):

        reservations = Reservation.get_all_published()

        data = []

        for reservation in reservations:
            data.append(reservation.data())

        return {'data': data}, HTTPStatus.OK

    @jwt_required
    def post(self):
        json_data = request.get_json()

        current_user = get_jwt_identity()

        reservation = Reservation(
                        title=json_data['title'],
#                        date=json_data['date'],
                        startTime=json_data['startTime'],
                        endTime=json_data['endTime'],
                        duration=json_data['duration'],
#                        is_publish=json_data['is_publish'],
                        user_id=current_user)


        reservation.save()

        return reservation.data(), HTTPStatus.CREATED

class ReservationResource(Resource):

    @jwt_optional
    def get(self, reservation_id):

        reservation = Reservation.get_by_id(reservation_id=reservation_id)

        if reservation is None:
            return {'message': 'Reservation not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation.is_publish == False and reservation.user_id != current_user:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        return reservation.data(), HTTPStatus.OK

    @jwt_required
    def put(self, reservation_id):

        json_data = request.get_json()

        reservation = Reservation.get_by_id(reservation_id=reservation_id)

        if reservation is None:
            return {'message': 'Reservation not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != reservation.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        Reservation.id = json_data['id']
        Reservation.title = json_data['title']
        Reservation.date = json_data['date']
        Reservation.startTime = json_data['startTime']
        Reservation.is_publish = json_data['isPublish']

        reservation.save()

        return reservation.data(), HTTPStatus.OK

    @jwt_required
    def delete(self, reservation_id):

        reservation = Reservation.get_by_id(reservation_id=reservation_id)

        if reservation is None:
            return {'message': 'Reservation not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != reservation.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        reservation.delete()

        return {}, HTTPStatus.NO_CONTENT

class ReservationPublishResource(Resource):

    @jwt_required
    def put(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'Reservation not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != room.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        reservation.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    @jwt_required
    def delete(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'Reservation not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != room.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        reservation.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
