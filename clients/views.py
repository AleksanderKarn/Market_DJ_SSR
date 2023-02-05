import datetime

import pytz
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from clients.forms import SigninForm, SignupForm
from clients.models import User
from clients.services import set_verify_token_and_send_mail


class SigninView(LoginView):
    template_name = 'users/login.html'
    form_class = SigninForm




class SignupView(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('users:register_success')

    def form_valid(self, form):
        if form.is_valid():

            self.object = form.save()
            set_verify_token_and_send_mail(self.object)
        return super().form_valid(form)


class SignupSuccessView(TemplateView):
    template_name = 'users/signup_success.html'

