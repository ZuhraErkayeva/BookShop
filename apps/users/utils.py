# from django.core.mail import send_mail
# from django.contrib.auth.tokens import default_token_generator
# from django.conf import settings
#
#
# def send_email_verification(user):
#     token = default_token_generator.make_token(user)
#     uid = user.pk
#     verification_link = f"http://localhost:8000/users/verify-email/{uid}/{token}/"
#
#     subject = "Emailingizni tasdiqlang"
#     message = f"Salom {user.username}, emailingizni tasdiqlash uchun quyidagi linkni bosing: {verification_link}"
#
#     send_mail(
#         subject,
#         message,
#         settings.DEFAULT_FROM_EMAIL,
#         [user.email],
#         fail_silently=False
#     )
#
#
#
# def send_reset_email(email, reset_url):
#     subject = "Parolni tiklash"
#     message = f"Parolingizni tiklash uchun quyidagi havolani bosing:\n\n{reset_url}"
#     send_mail(subject, message, "erkayevazuhra6@gmail.com", [email])
