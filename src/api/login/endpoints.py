from flask import Blueprint, request, jsonify
from ...models.entities.persona import Persona
from ...models.modelPersona import ModelPersona
from src import db

api = Blueprint('api', __name__)

@api.route('/getOne', methods=['POST'])
def getOne():
    try:
        data = request.get_json()
        correo = data.get('correo')
        contrasena = data.get('contrasena')
        
        user = Persona(0, 0, 0, 0, 0, 0, 0, correo, contrasena)

        persona = ModelPersona.readOne(db, user)
        
        if persona != None:
            return jsonify(persona)
        else:
            return jsonify({'message': 'No se encuentra'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@api.route('/getAll')
def getAll():
    try:
        personas = ModelPersona.read(db)
        
        return jsonify(personas)
    except Exception as e:
        return jsonify({'message' : str(e)}), 500