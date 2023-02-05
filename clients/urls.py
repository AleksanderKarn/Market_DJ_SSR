from django.contrib.auth.views import LogoutView
from django.urls import path

from clients.apps import ClientsConfig
from clients.views import SigninView, SignupView, SignupSuccessView

app_name = ClientsConfig.name

urlpatterns = [
    path('', SigninView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignupView.as_view(), name='register'),
    path('register/success/', SignupSuccessView.as_view(), name='register_success'),
]