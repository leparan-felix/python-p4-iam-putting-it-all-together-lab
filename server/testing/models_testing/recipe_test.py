import pytest
from sqlalchemy.exc import IntegrityError

from server.app import app
from server.models import db, Recipe

class TestRecipe:
    '''Recipe in models.py'''

    def test_has_attributes(self):
        '''has attributes title, instructions, and minutes_to_complete.'''
        
        with app.app_context():

            Recipe.query.delete()
            db.session.commit()

            recipe = Recipe(
                title="Delicious Shed Ham",
                instructions=(
                    "Or kind rest bred with am shed then. In"
                    " raptures building an bringing be. Elderly is detract"
                    " tedious assured private so to visited. Do travelling"
                    " companions contrasted it. Mistress strongly remember"
                    " up to. Ham him compass you proceed calling detract."
                    " Better of always missed we person mr. September"
                    " smallness northward situation few her certainty"
                    " something."
                ),
                minutes_to_complete=60,
            )

            db.session.add(recipe)
            db.session.commit()

            new_recipe = Recipe.query.filter(Recipe.title == "Delicious Shed Ham").first()

            assert new_recipe.title == "Delicious Shed Ham"
            assert new_recipe.minutes_to_complete == 60
            assert new_recipe.instructions.startswith("Or kind rest bred with am shed then.")

    def test_requires_title(self):
        '''requires each record to have a title.'''

        with app.app_context():

            Recipe.query.delete()
            db.session.commit()

            recipe = Recipe()

            with pytest.raises(IntegrityError):
                db.session.add(recipe)
                db.session.commit()

    def test_requires_50_plus_char_instructions(self):
        '''must raise either an IntegrityError or a custom ValueError if instructions are too short.'''

        with app.app_context():

            Recipe.query.delete()
            db.session.commit()

            with pytest.raises((IntegrityError, ValueError)):
                recipe = Recipe(
                    title="Generic Ham",
                    instructions="idk lol"  # too short
                )
                db.session.add(recipe)
                db.session.commit()
