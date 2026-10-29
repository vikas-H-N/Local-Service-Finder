
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("customer/", views.customer_dashboard, name="customer_dashboard"),
    path("provider/", views.provider_dashboard, name="provider_dashboard"),
]
