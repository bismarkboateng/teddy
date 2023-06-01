from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("signup/", views.Signup, name="signup"),
    path("login/", LoginView.as_view(template_name = "core/login.html", authentication_form = LoginForm), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
