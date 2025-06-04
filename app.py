from flask import Flask
from flask_restx import Api
from routes.email import api as email_ns
from dotenv import load_dotenv
load_dotenv()

import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    api = Api(
        app,
        title="Email API",
        version="1.0",
        description="Servicio para enviar correos electrónicos"
    )

    api.add_namespace(email_ns, path="/emails")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
