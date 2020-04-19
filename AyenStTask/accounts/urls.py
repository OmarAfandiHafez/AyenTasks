from django.urls import path, re_path
from rest_auth.views import LogoutView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token
from rest_auth.registration.views import VerifyEmailView
from . import views

urlpatterns = (
    path('signup/', views.SignupAPIView.as_view(), name='account_signup'),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
    path('login/', views.CustomLoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/', PasswordChangeView.as_view()),
    path('reset-password/', PasswordResetView.as_view()),
    path('reset-password/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view()),
    path('token-verify/', verify_jwt_token),
    path('token-refresh/', refresh_jwt_token),
)
