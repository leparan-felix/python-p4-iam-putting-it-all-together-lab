from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    instructions = db.Column(db.Text)
    minutes_to_complete = db.Column(db.Integer)

    def __repr__(self):
        return f"<Recipe {self.id} - {self.name}>"
