from django.urls import path
from soccer import views

app_name = 'soccer'

urlpatterns = [
    path('', views.index, name="index")
]
