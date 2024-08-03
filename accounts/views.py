from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
)
from django.contrib.auth import get_user_model
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView
)


User = get_user_model()


class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("task:index")

    def form_valid(self, form):
        response = super().form_valid(form)
       # username = form.cleaned_data.get("username")
       # age = form.cleaned_data.get("age")
        email = form.cleaned_data.get("email")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(
            email=email,
            # username=username,
            password=raw_pw, 
            #age=age,
        )
        login(self.request, user)
        return response

class UserDetail(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'

class UserUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_edit.html'

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.kwargs['pk']})

class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password_change.html'

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/user_detail.html'

class UserDelete(DeleteView):
    model = User
    template_name = 'accounts/user_delete.html'
    success_url = reverse_lazy('login')   
