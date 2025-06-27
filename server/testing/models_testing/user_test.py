# def test_creates_users_at_signup(app):
#     with app.app_context():
#         user = User(username="testuser", email="test@example.com", password="hashedpw")
#         db.session.add(user)
#         db.session.commit()

#         assert User.query.count() == 1
