from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.reservation import Reservation, reservation_list


# This is the resources/reservation.py for web app. It is kinda similiar from the earlier projects, so I kinda reused it
# Works fine as always.
class ReservationListResource(Resource):

    def get(self):

        data = []

        for reservation in reservation_list:
            if reservation.is_publish is True:
                data.append(reservation.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        reservation = Reservation(name=data['name'],
                                  room_size=data['room_size'],
                                  reservation_start=data['reservation_start'],
                                  reservation_end=data['reservation_end'])

        reservation_list.append(reservation)

        return reservation.data, HTTPStatus.CREATED


class ReservationResource(Resource):

    def get(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if
                            reservation.id == reservation_id and reservation.is_publish == True), None)

        if reservation is None:
            return {'message': 'instruction not found'}, HTTPStatus.NOT_FOUND

        return reservation.data, HTTPStatus.OK

    def put(self, reservation_id):
        data = request.get_json()

        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'Reservation not found'}, HTTPStatus.NOT_FOUND

        reservation.name = data['name']
        reservation.room_size = data['room_size']
        reservation.start = data['reservation_start']
        reservation.end = data['reservation_end']

        return reservation.data, HTTPStatus.OK

    def delete(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        reservation_list.remove(reservation)

        return {}, HTTPStatus.NO_CONTENT


class ReservationPublishResource(Resource):

    def put(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        reservation.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        reservation.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
