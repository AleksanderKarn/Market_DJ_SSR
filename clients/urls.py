from django.contrib.auth.views import LogoutView, PasswordResetConfirmView
from django.urls import path

from clients.apps import ClientsConfig
from clients.views import SigninView, SignupView, SignupSuccessView, UserEditProfileView, verify_email, \
    CustomPasswordResetView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, \
    CustomPasswordResetDoneView

app_name = ClientsConfig.name





urlpatterns = [

    path('', SigninView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignupView.as_view(), name='register'),
    path('register/success/', SignupSuccessView.as_view(), name='register_success'),
    path('update_profile/', UserEditProfileView.as_view(), name='update_profile'),

    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
   # path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/<uidb64>/confirm/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('verify/<str:token>/', verify_email, name='verify_email'),
]