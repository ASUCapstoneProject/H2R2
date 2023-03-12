from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .forms import WorkerSignUpForm, ContactForm, UserUpdateForm
from .models import User, Report, WaterQuality, Worker
from django.template import loader
from django.conf import settings
from .decorators import user_required, manager_required
import stripe
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives, send_mail, BadHeaderError
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages #import messages



class CustomLoginView(LoginView):
    template_name = 'basewater/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('report')


def datapage(request):
    return render(request,'basewater/datapage.html')


# Create your views here.
def test(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["email"]
            from_email = 'h2r2contact@gmail.com'
            email = 'rmkashya@asu.edu'
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [email])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect('home')
    return render(request,'basewater/test.html', {"form": form})
    # return render(request, 'basewater/test.html', context)

@method_decorator([login_required], name='dispatch')
class TaskList(ListView):
    model = Report
    context_object_name = 'report'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['report'] = context['report'].filter(user=self.request.user)
        context['complete_count'] = Report.objects.filter(user=self.request.user, complete=True).count()
        context['incomplete_count'] = Report.objects.filter(user=self.request.user, complete=False).count()
        # context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        # context['key'] = settings.STRIPE_SECRET_KEY
        return context

# @method_decorator([login_required, manager_required], name='dispatch')
class TaskCreate(CreateView):
    model = WaterQuality
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('report')


@login_required
def update_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated.')
            return redirect('report')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'basewater/User_form.html', {'form': form})

class WorkerSignUpView(CreateView):
    model = User
    form_class = WorkerSignUpForm
    template_name = 'basewater/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'worker'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        htmly = get_template('basewater/Email.html')
        d = { 'username': user }
        subject, from_email, to = 'welcome', 'h2r2contact@gmail.com', user.email
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        login(self.request, user)
        return redirect('report')

@login_required
def meeting(request):
     return render(request, 'basewater/meeting.html')

def charge(request):
    if request.method == 'POST': 
        charge = stripe.Charge.create( 
            amount=500,
            currency='usd',
            description='A Django charge', 
            source=request. POST['stripeToken']
        )
        return render (request, 'charge.html')




