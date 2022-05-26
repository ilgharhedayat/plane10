import datetime
import logging

import requests
from azbankgateways import bankfactories
from azbankgateways import default_settings as settings
from azbankgateways import models as bank_models
from azbankgateways.exceptions import AZBankGatewaysException
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

# from django.views.generic import View
#
# from .forms import PassengerForm
#
#
# # Create your views here.
#
#
# class ReserveCreateView(View):
#     form_class = PassengerForm
#     template_name = "passengers/reserve.html"
#
#     def get(self, request):
#         return render(request, self.template_name, {"form": self.form_class})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             cd = form.save(commit=False)
#             cd.reserver = request.user
#             cd.fly_code = request.POST.get("fly_code")
#             cd.save()
#             messages.success(request, "", "success")
#             return redirect()
#         else:
#             messages.error(request, "", "danger")
#         return render(request, self.template_name, {"form": form})
from django.views import View

from airlines.models import Airline
from passangers.models import Passenger

from .forms import PassengerForm
from .models import Passenger, Reservation


def home(request):
    return render(request, "index.html")


class PassengerView(View):
    template_name = "passengers/passengers.html"
    form_class = ""

    def get(self, request):
        info = {
            "airline_name": request.GET.get("airline_name"),
            "DepartureTime": request.GET.get("DepartureTime"),
            "ArrivalTime": request.GET.get("ArrivalTime"),
            "Destination": request.GET.get("Destination"),
            "date": request.GET.get('persian_date'),
            'origin': request.GET.get('origin_city_name0'),
            'destination': request.GET.get('destination_city_name')
        }
        print(request.GET.get('airline_name'))
        print("*" * 99)
        print(info.get('airline_name'))
        print(request.GET.get('persian_date'))

        return render(request, self.template_name, {"info": info})

    def post(self, request):
        print('elyas')
        print(request.POST)
        print(request.POST.get('airline_name'))

        return render(request, self.template_name)


class TripInfoView(View):
    def get(self, request):
        reserve_obj = Reservation.objects.filter(
            user=request.user, created=datetime.date.today()
        )
        return render(request, "passengers/infoSubmit.html", {"reserve": reserve_obj})


def go_to_gateway_view(request):
    amount = 1000
    user_mobile_number = "+989112221234"

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create()
        bank.set_request(request)
        bank.set_amount(amount)
        bank.set_client_callback_url(reverse("callback-gateway"))
        bank.set_mobile_number(user_mobile_number)  # اختیاری

        bank_record = bank.ready()

        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        raise e
