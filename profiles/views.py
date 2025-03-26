from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from profiles.models import Profile, Projects
from users.models import User
from .forms import ProfileForm
from .forms import ProjectsForm

@login_required
def profile_detail(request, username=None):
    if username is None:
        # Display the logged-in user's profile
        user = request.user
    else:
        # Display the profile of the specified username
        user = get_object_or_404(User, username=username)
    
    profile = get_object_or_404(Profile, user=user)
    
    context = {
        'profile_user': user,
        'profile': profile,
    }
    
    return render(request, 'profile/profile_detail.html', context)


@login_required
def edit_profilehead(request, id):
    profile = get_object_or_404(Profile, user_id=id)

    # Ensure the logged-in user owns the experience
    if profile.user != request.user:
        return HttpResponseForbidden("Unauthorized Action")

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile/edit_profilehead.html', {'form': form})


@login_required
def add_projects(request, username):
    if request.user.username != username:
        return HttpResponseForbidden("You are not authorized to add an projects to this profile.")

    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.profile = request.user.profile
            projects.save()
            return redirect('profile_detail', username=username)
    else:
        form = ProjectsForm()

    return render(request, 'profile/add_projects.html', {'form': form})

@login_required
def delete_projects(request, id):
    projects = get_object_or_404(Projects, id=id)

    # Ensure the logged-in user owns the experience
    if projects.profile.user != request.user:
        return HttpResponseForbidden("You are not authorized to delete this projects.")

    if request.method == 'POST':
        projects.delete()
        return redirect('profile_detail', username=request.user.username)
    return render(request, 'profile/confirm_delete.html', {'projects': projects})

@login_required
def edit_projects(request, id):
    projects = get_object_or_404(Projects, id=id)

    # Ensure the logged-in user owns the experience
    if projects.profile.user != request.user:
        return HttpResponseForbidden("You are not authorized to edit this projects.")

    if request.method == 'POST':
        form = ProjectsForm(request.POST, instance=projects)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', username=request.user.username)
    else:
        form = ProjectsForm(instance=projects)

    return render(request, 'profile/add_projects.html', {'form': form})