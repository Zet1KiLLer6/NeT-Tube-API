from django.core.mail import send_mail


def send_activation_code(email, code):
    send_mail(
        'NeT Tube API',
        f'Перейдите по этой ссылке, чтобы активировать аккаунт: \n\n http://localhost:8000/api/v1/account/activate/{code}',  # later will be template
        'netflix.py29.js19@gmail.com',
        [email]
    )

def send_forgot_password_code(email, code):
    send_mail(
        'NeT Tube API',
        f'Это ваш код для восстановления пароля, никому не показывайте его: {code}',  # later will be template
        'netflix.py29.js19@gmail.com',
        [email]
    )