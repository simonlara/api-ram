"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from family_datastructure import Family
family= Family('Doe')

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/member', methods=['POST', 'GET'])
def handle_members():
    if request.method=='GET':
        all=jsonify( family.get_all_members())
        return all,200

    if request.method=='POST':
        member = request.get_json()
        family.add_member(member)
        return member,200

@app.route('/member/<int:member_id>', methods=['GET','PUT','DELETE'])
def handle_member(member_id):
    member= family.get_member(member_id)
    if request.method=='GET':
       return jsonify(member), 200

    if request.method=='DELETE':
        family.delete_member(member_id)
        return jsonify(family._members), 200

    if request.method=='PUT':
        family.update_member(member_id)
        return jsonify(member), 200


# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
