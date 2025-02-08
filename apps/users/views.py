from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from apps.users.models import User
from apps.users.serializers import UserRegisterSerializer, UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]



class VerifyEmailView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        uid = request.GET.get("uid")
        token = request.GET.get("token")

        try:
            user = User.objects.get(pk=uid)  # Base64 decode qilish shart emas
        except User.DoesNotExist:
            return Response({"error": "Foydalanuvchi topilmadi"}, status=400)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"message": "Email muvaffaqiyatli tasdiqlandi"}, status=200)

        return Response({"error": "Noto‘g‘ri yoki eskirgan token"}, status=400)