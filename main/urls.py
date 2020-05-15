from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
]