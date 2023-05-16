from shop.views import *
from django.urls import path

from . import views

urlpatterns = [
    path("parts", views.ListPart.as_view()),
    path('parts/<pk>', PartDetailView.as_view())
    ]
