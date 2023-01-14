from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Worker, User


class WorkerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        worker = Worker.objects.create(user=user)
        return user