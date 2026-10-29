from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "services/home.html")


def customer_dashboard(request):
    return render(request, "services/customer_dashboard.html")


def provider_dashboard(request):
    return render(request, "services/provider_dashboard.html")
