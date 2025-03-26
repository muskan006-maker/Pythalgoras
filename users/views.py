# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import User
from .forms import CustomUserCreationForm
from .forms import EditUserForm
from django.urls import reverse
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import views

# User Signup (Only for Superadmins & Admins)
@login_required
def signup_view(request):
    """
     This is where one creates a new user. Only the admins/superadmins
     can create new users, anyone else is redirected to error page.
    """
    if not request.user.is_superuser and not request.user.is_superadmin() and not request.user.is_admin():
        return render(request, 'users/unauthorized.html')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_management')  # Redirect to user management after signup
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/signup.html', {'form': form})


# User Login
def login_view(request):
    """
    When a form is submitted with username and password,
    the request method shall be POST and first part of
    the if-else conditional will get executed. Otherwise,
    we just display the login page.
    """
    form = AuthenticationForm()  # Create an instance of the authentication form

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/login.html', {'form': form, 'error': 'Invalid credentials'})

    return render(request, 'users/login.html', {'form': form})




#  User Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# User Management (Only for Admins & Superadmins)
@login_required
def user_management_view(request):
    """
     Supplies a list of users for an admin or superadmin to work with.
     Superadmin can see everyone.
     Admins can see instructors and trainees
    """
    if not request.user.is_superuser and not request.user.is_superadmin() and not request.user.is_admin():
        return render(request, 'users/unauthorized.html')

    # Superadmins see all users except themselves
    if request.user.is_superadmin() or request.user.is_superuser:
        users = User.objects.exclude(id=request.user.id)  # Exclude self

    # Admins only see Instructors & Trainees (No other Admins or Superadmin)
    elif request.user.is_admin():
        users = User.objects.filter(role__in=['instructor', 'trainee'])

    return render(request, 'users/user_management.html', {'users': users})


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if not (request.user.is_superadmin() 
        or request.user.is_admin()
	or request.user.id == user.id ): return render(request, 'users/unauthorized.html')

    #<a href="{% url 'edit_user' user.id %}?next={{ request.path }}" class="btn btn-secondary">Edit</a>


    # Retrieve the 'next' value from the GET request
    next_url = request.GET.get('next', '')

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            if next_url:
                return redirect(next_url)
            else:
                return redirect('profile_detail', username=user.username)
    else:
        form = EditUserForm(instance=user)
    print("next: ",next_url)
    return render(request, 'users/edit_user.html', {'form': form, 'next': next_url})


# Deactivate a User (Only for Admins & Superadmins)
@login_required
def deactivate_user(request, user_id):
    if not request.user.is_superadmin() and not request.user.is_admin():
        return render(request, 'users/unauthorized.html')

    user = get_object_or_404(User, id=user_id)

    if user.is_superadmin():  # Prevent deactivating the Superadmin
        return render(request, 'users/unauthorized.html')

    user.is_active = False
    user.save()
    return redirect('user_management')


# Reactivate a User (Only for Admins & Superadmins)
@login_required
def reactivate_user(request, user_id):
    if not request.user.is_superadmin() and not request.user.is_admin():
        return render(request, 'users/unauthorized.html')

    user = get_object_or_404(User, id=user_id)
    user.is_active = True
    user.save()
    return redirect('user_management')


@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html')

#Custom view for password change
class CustomPasswordChangeView(views.PasswordChangeView):
      template_name = 'users/password_change.html' 
      success_url = reverse_lazy("custom_password_change_done")
@login_required
def custom_password_change_done(request):
    return render(request,'users/password_change_custom_done.html')
