from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")), # path to django allauth url to handle authentication
]
