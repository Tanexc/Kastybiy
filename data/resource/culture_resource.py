from flask import jsonify
from flask_restful import Resource, abort
from data.cuisine import Recipe
from data import db_session


class CultureResource(Resource):
    def get(self, id: int):
        abort_if_recipe_not_found(id)
        session = db_session.create_session()
        recipe = session.query(Recipe).get(id)
        info = recipe.to_dict()
        info["image"] = f"https://kastybiy.herokuapp.com/static/img/culture/cult_{id}.jpg"
        return jsonify({'culture': info})


class CultureListResource(Resource):
    def get(self):
        session = db_session.create_session()
        recipes = session.query(Recipe).all()
        a = []
        for item in recipes:
            info = item.to_dict()
            info["image"] = f"https://kastybiy.herokuapp.com/static/img/culture/cult_{item.id}.jpg"
            a.append(info)
        return jsonify({'culture': a})


def abort_if_recipe_not_found(id):
    session = db_session.create_session()
    recipe = session.query(Recipe).get(id)
    if not recipe:
        abort(404, message=f"Recipe with id = {id} not found")
