from django.urls import path
from . views import UserRegistrationView, UserLOginView, UserProfileView, UserChangePassword, SendPasswordResetEmailView, UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLOginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('change_password/', UserChangePassword.as_view(), name='change_password'),
    path('send_reset_password_email/', SendPasswordResetEmailView.as_view(), name='send_reset_password_email'),
    path('reset_password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset_password')
]