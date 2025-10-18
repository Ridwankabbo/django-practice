from django.urls import path
from . import views

urlpatterns = [
    path('all-users/', views.UsersApi.as_view(), name="all-users"),
    path('register-user/', views.UserRegistrationView.as_view(), name='register'),
    path('login-user/', views.LoginView.as_view(), name="login-user"),
    path('verify-opt/', views.VerifyOtpView.as_view(), name="verify-opt"),
    path('resend-opt/', views.ResendOtpView.as_view(), name="resend-otp"),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name="forgot-password"),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset-password')
]
