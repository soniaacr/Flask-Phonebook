from flask import Blueprint, request, jsonify
from helpers import token_required
from models import db, User, Contact, contact_schema, contacts_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/contacts', methods=['POST'])
@token_required
def create_contact():
    name = request.json['name']
    email = request.json['email']
    phone_number = request.json['phone_number']
    address = request.json['address']
    user_token = request.current_user_token.token
    print(f'BIG TESTER: {user_token}')
    contact = Contact(name=name, email=email, phone_number=phone_number, address=address, user_token=user_token)
    db.session.add(contact)
    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)

@api.route('/contacts', methods=['GET'])
@token_required
def get_contact():
    a_user = request.current_user_token.token 
    contacts = Contact.query.filter_by(user_token=a_user).all()
    response = contacts_schema.dump(contacts)
    return jsonify(response)
