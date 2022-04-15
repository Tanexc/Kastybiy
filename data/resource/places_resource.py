from flask import jsonify
from flask_restful import Resource, abort
from data.places import Place
from data import db_session


class PlaceResource(Resource):
    def get(self, id: int):
        session = db_session.create_session()
        place = session.query(Place).get(id)
        info = place.to_dict()
        info["image"] = f"https://kastybiy.herokuapp.com/static/img/places/place_{id}.jpg"
        return jsonify({'place': info})


class PlaceListResource(Resource):
    def get(self):
        session = db_session.create_session()
        places = session.query(Place).all()
        a = []
        for item in places:
            info = item.to_dict()
            info["image"] = f"https://kastybiy.herokuapp.com/static/img/places/place_{item.id}.jpg"
            a.append(info)
        return jsonify({'places': a})