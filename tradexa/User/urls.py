from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("signup", views.signup, name="signup"),
    path("login", views.login_func, name="login"),
    path("logout", views.logout_func, name="logout"),
    path("createpost", views.createpost, name="createpost"),

]