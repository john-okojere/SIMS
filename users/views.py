from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import StudentRegisterForm, StaffRegisterForm
from django.contrib.auth.decorators import user_passes_test


class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')

# Student Registration View
def student_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to student dashboard
    else:
        form = StudentRegisterForm()
    return render(request, 'student_register.html', {'form': form})

# Staff Registration View (For Lecturers and Clinic Staff)
def staff_register(request):
    if request.method == 'POST':
        form = StaffRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to staff dashboard
    else:
        form = StaffRegisterForm()
    return render(request, 'staff_register.html', {'form': form})

# Superuser creation (Admin)
@user_passes_test(lambda u: u.is_superuser)
def create_superuser(request):
    # Django's built-in createsuperuser command can be used for this purpose
    return redirect('admin/')
