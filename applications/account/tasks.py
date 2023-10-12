from config.celery import app
from .services import send_activation_code, send_forgot_password_code

@app.task
def celery_send_activation_code(email, code):
    send_activation_code(email, code)

@app.task
def celecry_send_forgot_password_code(email, code):
    send_forgot_password_code(email, code)