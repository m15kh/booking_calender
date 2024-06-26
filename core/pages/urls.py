from django.urls import path
from .views import HomePageView, TestPageView, ListBarberPageView, ComponentPageView

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("test/", TestPageView.as_view(), name="test"),
    path("list_barber/", ListBarberPageView.as_view(), name="list_barber"),
    path("components/", ComponentPageView.as_view(), name="components"),
]
