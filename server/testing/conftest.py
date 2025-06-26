from server.app import create_app

@pytest.fixture(scope="module") # type: ignore
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all() # type: ignore
        yield app
        db.session.remove() # type: ignore
        db.drop_all() # type: ignore
