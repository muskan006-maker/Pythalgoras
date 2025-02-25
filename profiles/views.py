from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

@login_required
def profile_view(request):
    """Displays the profile if it exists, otherwise redirects to profile creation."""
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "profiles/profile_detail.html", {"profile": profile})

@login_required
def edit_profile(request):
    """Handles profile creation and editing."""
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile_view")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "profiles/profile_form.html", {"form": form})
