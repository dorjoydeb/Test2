from django.urls import path
from . import views

app_name = 'Main_app'

urlpatterns = [
    path('', views.Home, name='App_home'),
    path('contact_info/', views.Contact_info, name='App_contact')
]