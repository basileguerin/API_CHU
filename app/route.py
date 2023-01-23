from flask import request, jsonify, render_template
from app import app
from .db import get_db_config, db_connect

path = "/home/zile/iadev-python/py-sql/API/API_CHU/config.json"
config = get_db_config(path)

myDB = db_connect(config)
cursor = myDB.cursor()
dbOK = myDB.is_connected()

@app.route('/')
def index():
    return render_template('index.html')

#EMPLOYES
@app.route('/employe', methods=['GET'])
def get_db_employe():
    query = """SELECT * FROM employé_informatique"""
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/employe/<int:id>', methods=["GET"])
def get_employe(id):
    query = f"""SELECT * FROM employé_informatique 
    WHERE id='{id}'"""
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/employe', methods=["PUT"])
def update_employe():
    data = request.get_json()
    query = f"""UPDATE employé_informatique 
    SET nom="{data['nom']}", prenom="{data['prenom']}", age="{data['age']}", 
    profession="{data['profesion']}" 
    WHERE id='{data['id']}';"""
    cursor.execute(query)
    myDB.commit()
    result_db = get_db_employe()
    return result_db

@app.route('/employe', methods=["POST"])
def add_employe():
    data = request.get_json()
    query = f"""INSERT INTO employé_informatique(nom, prenom, age, profession) 
    VALUES ("{data['nom']}", "{data['prenom']}", "{data['age']}", 
    "{data['profession']}");"""
    cursor.execute(query)
    myDB.commit()
    result_db = get_db_employe()
    return result_db

@app.route('/employe', methods=["DELETE"])
def delete_employe():
    data = request.get_json()
    query=f"""DELETE FROM employé_informatique 
    WHERE id='{data['id']}';"""
    cursor.execute(query)
    myDB.commit()
    result_db = get_db_employe()
    return result_db

#MATERIEL
@app.route('/materiel', methods=['GET'])
def get_db_matos():
    query = """SELECT * FROM materiel"""
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/materiel/<int:id>', methods=["GET"])
def get_matos(id):
    query = f"""SELECT * FROM materiel 
    WHERE id='{id}'"""
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/materiel', methods=["PUT"])
def update_matos():
    data = request.get_json()
    query = f"""UPDATE materiel 
    SET nom_du_produit="{data['nom_du_produit']}", 
    dimensions="{data['dimensions']}", etat="{data['etat']}" 
    WHERE id='{data['id']}';"""
    cursor.execute(query)
    myDB.commit()
    result_db = get_db_matos()
    return result_db

@app.route('/materiel', methods=["POST"])
def add_matos():
    data = request.get_json()
    query = f"""INSERT INTO materiel(nom_du_produit, dimensions, etat)
    VALUES ("{data['nom_du_produit']}", "{data['dimensions']}", 
    "{data['etat']}");"""
    cursor.execute(query)
    myDB.commit()
    result_db = get_db_matos()
    return result_db

@app.route('/materiel', methods=["DELETE"])
def delete_matos():
    data = request.get_json()
    query=f"""DELETE FROM materiel 
    WHERE id="{data['id']}";"""
    cursor.execute(query)
    myDB.commit()
    result_db = get_db_matos()
    return result_db
