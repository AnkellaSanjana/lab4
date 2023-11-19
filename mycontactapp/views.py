from django.shortcuts import render
from .models import Contact

# Create your views here.


def index(request):
    return render(request, "mycontactapp/index.html")


def help_page(request):
    return render(request, "mycontactapp/help.html")


def contacts(request):
    contact_list = Contact.objects.order_by("first_name")
    contact_dict = {"contacts": contact_list}
    return render(request, "mycontactapp/contacts.html", context=contact_dict)
