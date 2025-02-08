from django.urls import path

from apps.users.views import UserCreateView,UserListView,UserDetailView, VerifyEmailView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
]