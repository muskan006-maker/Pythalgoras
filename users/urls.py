from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy
from .views import (
    signup_view, login_view, logout_view, 
    user_management_view, deactivate_user, 
    edit_user, reactivate_user, dashboard_view,
)

urlpatterns = [
    # Authentication Routes
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Dashboard (for logged-in users)
    path('dashboard/', dashboard_view, name='dashboard'),

    # User Management (Admins & Superadmins)
    path('manage/', user_management_view, name='user_management'),
    path('edit/<int:user_id>/', edit_user, name='edit_user'),
    path('deactivate/<int:user_id>/', deactivate_user, name='deactivate_user'),
    path('reactivate/<int:user_id>/', reactivate_user, name='reactivate_user'),
   path('password_custom_change/',    
          auth_views.PasswordChangeView.as_view(
          template_name='users/password_change.html', 
          success_url = reverse_lazy('password_change_custom_done')
          ),
          name='password_custom_change'
),
path('password_custom_change/done/', 
          auth_views.PasswordChangeDoneView.as_view(
          template_name='users/password_change_custom_done.html', 
),          
name='password_change_custom_done'),

# Password Reset (Forgot Password)
path('custom_password_reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html',
             success_url=reverse_lazy('custom_password_reset_done')
         ), 
         name='custom_password_reset'),

# Password Reset Done (Email Sent Confirmation)
path('custom_password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done_custom.html'),
name='custom_password_reset_done'),
# Password Reset Confirm (User Sets New Password)
path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             success_url=reverse_lazy('password_reset_complete')
         ), 
         name='password_reset_confirm'),
# Password Reset Complete (Reset Successful Message)
path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
]

