from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
path('password_custom_change/',    
          auth_views.PasswordChangeView.as_view(
          template_name='registration/password_change.html', 
          success_url = reverse_lazy('password_change_custom_done')
          ),
          name='password_custom_change'
),
path('password_custom_change/done/', 
          auth_views.PasswordChangeDoneView.as_view(
          template_name='registration/password_change_custom_done.html', 
),          
name='password_change_custom_done'),

# Password Reset (Forgot Password)
path('custom_password_reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html',
             success_url=reverse_lazy('custom_password_reset_done')
         ), 
         name='custom_password_reset'),

# Password Reset Done (Email Sent Confirmation)
path('custom_password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done_custom.html'),
name='custom_password_reset_done'),
# Password Reset Confirm (User Sets New Password)
path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html',
             success_url=reverse_lazy('password_reset_complete')
         ), 
         name='password_reset_confirm'),
# Password Reset Complete (Reset Successful Message)
path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ), 
         name='password_reset_complete'),


path("accounts/",include("django.contrib.auth.urls")),
path("dashboard/",views.dashboard, name='dashboard'),
path("signup/",views.signup, name='signup'),
]
