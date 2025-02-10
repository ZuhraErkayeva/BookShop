from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from apps.users.models import User

user = User.objects.get(email="erkayevazuhra6@gmail.com")  # O'zingiz xohlagan userni tanlang
uid = urlsafe_base64_encode(force_bytes(user.pk))
token = default_token_generator.make_token(user)

verification_link = f"http://127.0.0.1:8000/users/verify-email/?uid={uid}&token={token}"
print("Tasdiqlash havolasi:", verification_link)
