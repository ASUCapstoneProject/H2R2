from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Worker, User


class WorkerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        worker = Worker.objects.create(user=user)
        return user

class ContactForm(forms.Form):
    email = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']