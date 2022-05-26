import json
import requests
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from airlines.models import Airline
from passangers.models import Passenger

from .models import Airline


class SearchListView(View):
    template_name = "airlines/search.html"

    def get(self, request):
        # available_trips = ''
        airlines_list = Airline.objects.all()
        for airline in airlines_list:
            trips = requests.get(
                f"http://zv.nirasoftware.com:882/AvailabilityJS.jsp?AirLine={airline.symbol}&cbSource={request.GET.get('source')}&cbTarget={request.GET.get('target')}&cbDay1={request.GET.get('date')}&cbMonth1={request.GET.get('date2')}&cbAdultQty={request.GET.get('adult', 0)}&cbChil%20dQty={request.GET.get('child', 0)}&cbInfantQty={request.GET.get('infant', 0)}&OfficeUser={airline.username}&OfficePass={airline.password}"
            )

            a = json.loads(trips.content)
            trip_list = a["AvailableFlights"]
            flight_count = 0
            for i in trip_list:
                i["image"] = airline.logo.url
                i["airline_name"] = airline.name
                i["DepartureTime"] = i["DepartureDateTime"][11:]
                i["ArrivalTime"] = i["ArrivalDateTime"][11:]
                flight_count += 1

            print(trip_list)

        request.session["passenger_info"] = {
            "adult": request.GET.get("adult", 0),
            "child": request.GET.get("child", 0),
            "infant": request.GET.get("infant", 0),
        }

        return render(
            request,
            self.template_name,
            {"trip_list": trip_list, "flight_count": flight_count},
        )


{
    'THR': 'تهران',
    'MHD': 'مشهذ',
}
