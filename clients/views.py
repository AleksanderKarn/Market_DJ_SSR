from datetime import datetime

import pytz
from django.conf import settings
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, \
    PasswordResetDoneView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from clients.forms import SigninForm, SignupForm, CustomEditUserForm, CustomPasswordResetForm
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

class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/update_users.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('products:list')

    def get_object(self, queryset=None):
        """ при изменении профиля дает возможность
        не задавать ID пользователя и не светить его в URL """
        return self.request.user


def verify_email(request, token):
    current_user = User.objects.filter(verify_token=token).first()
    if current_user:
        _now = datetime.now(pytz.timezone(settings.TIME_ZONE))
        if _now > current_user.verify_token_expired:
            current_user.delete()
            return render(request, 'users/verify_failed.html')

        current_user.is_active = True
        current_user.verify_token = None
        current_user.verify_token_expired = None
        current_user.save()
        return redirect('users:login')

    return render(request, 'users/verify_failed.html')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('users:password_reset_done')
    email_template_name = 'users/email_reset.html'
    from_email = settings.EMAIL_HOST_USER

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/reset_done.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/reset_complete.html'