from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import MyUserCreationForm


def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = MyUserCreationForm()
    return render(request, 'register.html', {'form': form})


