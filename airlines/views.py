import requests
from django.shortcuts import render
from django.views.generic import View

from .models import Airline


# Create your views here.
class SearchListView(View):
    def get(self, request, source, target, day, month, adult=0, child=0, infant=0):
        available_trips = {}
        airlines_list = Airline.objects.all()
        for airline in airlines_list:
            trips = requests.get(
                f"{airline.base_url} +=/AvailabilityFareJS.jsp?AirLine={airline.symbol}&cbSource={source}&cbTarget={target}&cbDay1={day}&cbMonth1={month}&DepartureDate=&cbAdultQty={adult}&cbChildQty={child}&cbInfantQty={infant}&OfficeUser{airline.username}&OfficePass={airline.password}"
            )
            airlines_list.update(trips.content, airline.logo)

        return render(request, "", {"trip_list": available_trips})
