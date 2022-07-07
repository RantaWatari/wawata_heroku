from flask import Flask,current_app
import os

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        #DATABASE = os.path.join("postgresql://postgres:0829@localhost:5432/postgres")
        DATABASE = os.path.join('postgres://fzqtnqpvwbibyn:bb4eb6098100999c883fe1ab374a046394f8db35bc93e24ee75d2a8a2b8d2360@ec2-3-228-235-79.compute-1.amazonaws.com:5432/d20m8qevefnne7postgres://ysbwuosrjdfhgh:8b051cb08b652e9001292338f20ef2f82d4199edc4e13acf9c5131679bb4f716@ec2-3-226-163-72.compute-1.amazonaws.com:5432/dvataoqaroqce'
')
    )

    from flask_file import server
    app.register_blueprint(server.bp)

    from flask_file import db_control
    app.teardown_appcontext(db_control.close_db)
    app.cli.add_command(db_control.init_db)

    return app
