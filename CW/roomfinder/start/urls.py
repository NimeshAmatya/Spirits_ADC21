from . import views
from django.urls import path

app_name = "start"

urlpatterns = [
	path('', views.home, name="home"),
	path("register/", views.register, name="register"),
]