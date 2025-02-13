from django.urls import include, path
from . import views

urlpatterns = [

path("accounts/", include("django.contrib.auth.urls")),
path("signup/",views.signup, name='signup'),
path("dashboard/",views.dashboard, name='dashboard'),

]
