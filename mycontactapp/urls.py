# mycontactapp/urls.py
from django.urls import path
from . import views

app_name = "mycontactapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("help/", views.help_page, name="help"),
    path("contacts/", views.contacts, name="contacts"),
]
