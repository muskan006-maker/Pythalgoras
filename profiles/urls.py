from django.urls import path
import profiles.views as views

urlpatterns = [
    path('profile/', views.profile_detail, name='profile'),  # Logged-in user's profile
    path('profile/<str:username>/add_projects/', views.add_projects, name='add_projects'),
    path('projects/edit/<int:id>/', views.edit_projects, name='edit_projects'),
    path('projects/delete/<int:id>/', views.delete_projects, name='delete_projects'),
    path('profilehead/edit/<int:id>/', views.edit_profilehead, name='edit_profilehead'),

    path('profile/<str:username>/', views.profile_detail,name='profile_detail'),  # View another user's profile
    #path('profile/<str:username>/edit/', edit_profile_view, name='edit_profile'),  # Edit profile (restricted to owner/admin)
]