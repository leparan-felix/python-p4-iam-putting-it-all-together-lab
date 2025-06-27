from flask import Blueprint, jsonify
from .models import Recipe

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "API is working!"})

@main.route('/recipes')
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "instructions": r.instructions,
        "minutes_to_complete": r.minutes_to_complete
    } for r in recipes])
