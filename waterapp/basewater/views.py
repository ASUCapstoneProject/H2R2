from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import WorkerSignUpForm
from .models import User
from django.template import loader

from .decorators import user_required, manager_required


class CustomLoginView(LoginView):
    template_name = 'basewater/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

# Create your views here.
def test(request):
     return render(request, 'basewater/test.html')

class WorkerSignUpView(CreateView):
    model = User
    form_class = WorkerSignUpForm
    template_name = 'basewater/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'worker'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

