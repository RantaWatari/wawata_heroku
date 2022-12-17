from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE = os.path.join("postgresql://postgres:0829@localhost:5432/postgres")
    )

    from flask_file import db_control
    app.teardown_appcontext(db_control.close_db)
    app.cli.add_command(db_control.init_db)
    app.cli.add_command(db_control.clean_db)
    
    from flask_file import server
    app.register_blueprint(server.bp)


    return app
