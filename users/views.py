# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful registration
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

# Or you can simply include the LoginView directly in your URLs
from django.contrib.auth.views import LogoutView
