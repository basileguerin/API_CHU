from app import app, db

TESTER_RECUPERATION_CONFIG_JSON = False

if __name__ == "__main__":
    if(TESTER_RECUPERATION_CONFIG_JSON):
        config = db.get_db_config("config.json")
        print(config)
    app.run(debug = True)
