from app.db import get_db_config, db_connect
import json

path = "/home/zile/iadev-python/py-sql/API/API_CHU/config.json"
config = get_db_config(path)

myDB = db_connect(config)
cursor = myDB.cursor()
dbOK = myDB.is_connected()

def populate_tables():
    """Remplit les tables materiel et employe_informatique a partir
    des données contenues dans le fichier data.json"""

    f = open('/home/zile/iadev-python/py-sql/API/API_CHU/data.json')
    data = json.load(f)

    for matos in data['materiel']:
        values = list(matos.values())
        keys = list(matos.keys())
        id = keys[0]
        nom_du_produit = values[0][0]
        dimensions = values[0][1]
        etat = values[0][2]
        query = f"""INSERT INTO materiel 
        VALUES ("{id}", "{nom_du_produit}", "{dimensions}", "{etat}");"""
        cursor.execute(query)
        myDB.commit()

    for employe in data["employé.e informatique"]:
        values = list(employe.values())
        keys = list(employe.keys())
        id = keys[0]
        nom = values[0][0]
        prenom = values[0][1]
        age = values[0][2]
        profession = values[0][3]
        query = f"""INSERT INTO employé_informatique 
        VALUES ("{id}", "{nom}", "{prenom}", "{age}", "{profession}");"""
        cursor.execute(query)
        myDB.commit()

if __name__ == "__main__":
    populate_tables()