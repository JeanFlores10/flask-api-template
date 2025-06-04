import os

class Config:
    EMAIL_USER = os.getenv("EMAIL_USER", "tu_email@gmail.com")
    EMAIL_PASS = os.getenv("EMAIL_PASS", "tu_contraseña_de_app")
