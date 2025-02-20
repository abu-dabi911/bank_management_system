from django.urls import path
from .views import login_view, dashboard_view, logout_view, register_view

urlpatterns = [
    path("", login_view, name="home"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),  # Новый маршрут регистрации
    path("dashboard/", dashboard_view, name="dashboard"),
    path("logout/", logout_view, name="logout"),
]
