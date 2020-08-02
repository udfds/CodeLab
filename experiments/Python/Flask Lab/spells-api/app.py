from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow
import os

# -----------------------------------------------------------------
# Application setup
# -----------------------------------------------------------------
app = Flask(__name__)
base_directory = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(base_directory, 'spells.db')

datababse = SQLAlchemy(app)
marsh = Marshmallow(app)

# -----------------------------------------------------------------
# Database setup
# -----------------------------------------------------------------


@app.cli.command('db_create')
def db_create():
    datababse.create_all()
    print("-- Database created!")


@app.cli.command('db_drop')
def db_drop():
    datababse.drop_all()
    print("-- Database dropped!")


@app.cli.command('db_seed')
def db_seed():
    spell_1 = Spell(title="Energy bolt", school="Wizard", rank=1)
    spell_2 = Spell(title="Sleep", school="Wizard", rank=1)
    spell_3 = Spell(title="Magic shield", school="Wizard", rank=1)
    spell_4 = Spell(title="Surespell", school="Wizard", rank=2)
    spell_5 = Spell(title="Magic missile", school="Wizard", rank=2)
    spell_6 = Spell(title="Quick cast", school="Wizard", rank=3)

    datababse.session.add(spell_1)
    datababse.session.add(spell_2)
    datababse.session.add(spell_3)
    datababse.session.add(spell_4)
    datababse.session.add(spell_5)
    datababse.session.add(spell_6)
    print("-- Database seed!")


# -----------------------------------------------------------------
# Class setup
# -----------------------------------------------------------------

class Spell(datababse.Model):
    __tablename__ = "spells"
    spell_id = Column(Integer, primary_key=True)
    title = Column(String)
    school = Column(String)
    rank = Column(Integer)

# -----------------------------------------------------------------
# Schema setup
# -----------------------------------------------------------------


class SpellSchema(marsh.Schema):
    class Meta:
        fields = ('spell_id', 'title', 'school', 'rank')


spell_schema = SpellSchema()
spells_schema = SpellSchema(many=True)

# -----------------------------------------------------------------
# API setup
# -----------------------------------------------------------------


@app.route('/', methods=['GET'])
def index():
    return jsonify(message="Hello!")


@app.route('/spells', methods=['GET'])
def spell_list():
    spell_list = Spell.query.all()
    result = spells_schema.dump(spell_list)
    return jsonify(result)


@app.route('/spells/<int:spell_id>', methods=['GET'])
def spell_details(spell_id: int):
    spell = Spell.query.filter_by(spell_id=spell_id).first()
    if spell:
        result = spell_schema.dump(spell)
        return jsonify(result)
    else:
        return jsonify(message="Spell not found"), 404


if __name__ == '__main__':
    app.run()
