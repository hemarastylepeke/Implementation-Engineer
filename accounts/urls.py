from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),  # Landng page
    path("success", views.success_page, name="success_page"),  # Landng page
]