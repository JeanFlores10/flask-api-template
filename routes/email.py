from flask import request, current_app
from flask_restx import Namespace, Resource, fields
import smtplib
from email.message import EmailMessage

api = Namespace("emails", description="Operaciones de correo electrónico")

email_model = api.model("Email", {
    "to": fields.String(required=True, description="Correo del destinatario"),
    "subject": fields.String(required=True, description="Asunto del correo"),
    "message": fields.String(required=True, description="Mensaje del correo")
})

@api.route("/send")
class SendEmail(Resource):
    @api.expect(email_model)
    def post(self):
        """Envía un correo electrónico"""
        data = request.json
        email_user = current_app.config["EMAIL_USER"]
        email_pass = current_app.config["EMAIL_PASS"]

        try:
            msg = EmailMessage()
            msg["Subject"] = data["subject"]
            msg["From"] = email_user
            msg["To"] = data["to"]
            msg.set_content(data["message"])

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(email_user, email_pass)
                smtp.send_message(msg)

            return {"message": "Correo enviado con éxito"}, 200

        except Exception as e:
            return {"error": str(e)}, 500
