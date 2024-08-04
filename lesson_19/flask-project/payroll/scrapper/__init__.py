import os

from flask import Flask
from payroll import scrapper, books

def create_app():
    app = Flask(__name__, instance_relative_config = True)
    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    app.register_blueprint(scrapper.bp)
    app.register_blueprint(books.bp)

    return app