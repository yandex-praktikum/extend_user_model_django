from django.db import transaction
from django.shortcuts import render

from .forms import ProfileForm, UserForm
from .models import User


def profile(request):
    users = User.objects.all().select_related('profile')

    return render(request, 'users/profile.html', {'users': users})

