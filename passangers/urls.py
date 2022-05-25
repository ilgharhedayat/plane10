from django.urls import path

from .views import PassengerView, TripInfoView, go_to_gateway_view, home

app_name = "passengers"
urlpatterns = [
    path("", home, name="home"),
    path("", TripInfoView.as_view(), name="trip"),
    path("", go_to_gateway_view, name="pay"),
    path("passenger/", PassengerView.as_view(), name="passenger"),
]
