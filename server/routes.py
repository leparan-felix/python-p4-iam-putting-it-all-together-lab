from flask import request, jsonify, Blueprint
from server.models import db, User

bp = Blueprint('api', __name__)

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    bio = data.get('bio')
    image_url = data.get('image_url')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 422

    user = User(
        username=username,
        password=password,
        bio=bio,
        image_url=image_url
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'id': user.id,
        'username': user.username,
        'bio': user.bio,
        'image_url': user.image_url
    }), 201
