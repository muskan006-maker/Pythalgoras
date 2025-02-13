from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm

# View handler for signup function
def signup(request):
    """
     When a form submission has occurred the 
     code in the "if-block" executes otherwise
     code in the "else-block" execures
    """

    if request.method == "POST":
        #This class is imported above
        form = UserCreationForm(request.POST) 
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
	    #Login function is also imported above
            login(request, user)
            return redirect(reverse("dashboard"))
    else:
	#if the form is not submitted that simply show the form
        form = UserCreationForm()
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

#dashboard function
def dashboard(request):
    return render(request, "registration/dashboard.html")



