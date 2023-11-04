from weatherApp import views
from django.urls import path

urlpatterns=[
    path('firstfunction/',views.firstfunction,name="firstfunction"),
]