from shop.views import *
from django.urls import path

from . import views
from .views import Logout

urlpatterns = [
    path('logout/', Logout.as_view()),
    ]
