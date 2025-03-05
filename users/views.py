from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")
# View handler for signup function
def signup(request):
    """
     When a form submission has occured the 
     code in the "if-block" executes otherwise
     code in the "else-block" execures
    """
    if request.method == "POST":
        #This class is imported above
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
	    #Login function is also imported above
            login(request, user)
            return redirect(reverse("dashboard"))
    else:
	#if the form is not submitted that simply show the form
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})
#Custom view for password change
class CustomPasswordChangeView(views.PasswordChangeView):
      template_name = 'users/password_change.html' 
      success_url = reverse_lazy("custom_password_change_done")
@login_required
def custom_password_change_done(request):
    return render(request,'users/password_change_custom_done.html')

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
            return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    return render(request, 'users/login.html', {'form': form})

