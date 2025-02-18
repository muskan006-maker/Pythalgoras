from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from.forms import CustomUserCreationForm 


# Create your views here.
def dashboard(request):
    return render(request, "registration/dashboard.html")

# View handler for signup function
def signup(request):
    """
     When a form submission has occured the 
     code in the "if-block" executes otherwise
     code in the "else-block" execures
    """

    if request.method == "POST":
        #This class is imported above
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
	    #Login function is also imported above
            login(request, user)
            return redirect(reverse("dashboard"))
    else:
	#if the form is not submitted that simply show the form
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})