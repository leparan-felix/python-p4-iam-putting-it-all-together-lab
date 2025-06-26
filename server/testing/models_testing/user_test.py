from server.models import db, User

def test_creates_users_at_signup(client, app):
    with app.app_context():
        User.query.delete()
        db.session.commit()

    response = client.post('/signup', json={
        'username': 'ashketchum',
        'password': 'pikachu',
        'bio': "I wanna be the very best\nLike no one ever was",
        'image_url': 'https://cdn.vox-cdn.com/uploads/chorus_asset/file.jpg'
    })

    assert response.status_code == 201
    data = response.get_json()
    assert data['username'] == 'ashketchum'
