import datetime
import json
import logging
import json
from django.http import HttpResponse
import requests
from azbankgateways import bankfactories
from azbankgateways import default_settings as settings
from azbankgateways import models as bank_models
from azbankgateways.exceptions import AZBankGatewaysException
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.conf import settings
from .models import Passenger, Reservation
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

    def setup(self, request, *args, **kwargs):
        self.info = {
            "airline_name": request.GET.get("airline_name"),
            "DepartureTime": request.GET.get("DepartureTime"),
            "ArrivalTime": request.GET.get("ArrivalTime"),
            "Destination": request.GET.get("Destination"),
            "date": request.GET.get('persian_date'),
            'origin': request.GET.get('origin_city_name'),
            'destination': request.GET.get('destination_city_name')
        }
        self.airline = Airline.objects.get(name=self.info.get('airline_name'))
        super(PassengerView, self).setup(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"info": self.info})

    def post(self, request):
        reserve = Reservation.objects.create(
            user_id=request.user.id,
            air_line=self.airline,
            fly_code=self.info.get(''),
            source=self.info.get('origin'),
            target=self.info.get('destination'),
            date='0',
            email='me@parsa.best',
            phone_number='0',
            paid=False
        )
        passengers = []
        for key, value in dict(request.POST).items():
            for i in range(0, len(value)):
                if len(passengers) > i:
                    passenger = passengers[i]
                else:
                    passenger = Passenger()
                    passenger.day = 0
                    passenger.month = 0
                    passenger.year = 0
                    passenger.price = 0
                    passenger.reserve = reserve
                if key == 'latinName':
                    passenger.en_name = value[i]
                elif key == 'latinFamilyName':
                    passenger.en_family = value[i]
                elif key == 'gender':
                    passenger.gender = value[i]
                elif key == 'nationalCode':
                    passenger.national_code = value[i]
                elif key == 'name':
                    passenger.ir_name = value[i]
                elif key == 'familyName':
                    passenger.ir_family = value[i]
                if len(passengers) > i:
                    passengers[i] = passenger
                else:
                    passengers.append(passenger)

        Passenger.objects.bulk_create(passengers)
        return render(request, self.template_name)


class TripInfoView(View):
    def get(self, request):
        reserve_obj = Reservation.objects.first()
        print(reserve_obj.fly_code)
        return render(request, "passengers/infoSubmit.html", {"reserve": reserve_obj})


class CancelTicketView(View):
    def get(self, request, reserve_id):
        reserve_obj = get_object_or_404(Reservation, id=reserve_id)
        reserve_obj.delete()
        return redirect('passengers:home')


class Reserve(View):
    def get(self, request):
        reserve_obj = Reservation.objects.first()
        # for i in reserve_obj.
        requests.get(
            f'{reserve_obj.air_line.base_url}/ReservJS?AirLine={reserve_obj.air_line.symbol}&cbSource={reserve_obj.source}&cbTarget={reserve_obj.target}Q&FlightClass={reserve_obj.flight_class}&FlightNo={reserve_obj.flight_no}&Day&Month&No=1&edtName1={reserve_obj.first_name}&edtLast1={reserve_obj.last_name}&edtAge1={reserve_obj.age}&edtID1={reserve_obj.national_code}&edtContact={reserve_obj.phone_number}&DepartureDate=2022-03-03&OfficeUser={reserve_obj.air_line.username}&OfficePass{reserve_obj.air_line.password}')


def go_to_gateway_view(request):
    amount = 1000
    user_mobile_number = "+989112221234"
    info = {
        'ResNum': '111111',
        'amount': amount,
        'cell': user_mobile_number,
    }
    return render(request, 'passengers/payTest.html', {'info': info})
    # factory = bankfactories.BankFactory()
    # try:
    #     bank = factory.auto_create()
    #     bank.set_request(request)
    #     bank.set_amount(amount)
    #     bank.set_client_callback_url(reverse("callback-gateway"))
    #     bank.set_mobile_number(user_mobile_number)  # ??????????????
    #
    #     bank_record = bank.ready()
    #
    #     return bank.redirect_gateway()
    # except AZBankGatewaysException as e:
    #     logging.critical(e)
    #     # TODO: redirect to failed page.
    #     raise e


def cities(request):
    # re = requests.get('https://api.vhotel.ir/api/V4/cities', auth=('admin', "iEol5iBJjFCRKIBA"))
    # data = re.text
    data = {

        "ABD": "????????????",

        "AKW": "??????????????",

        "AEU": "??????????????",

        "AJK": "????????",

        "ADU": "????????????",

        "OMH": "????????????",

        "IFN": "????????????",

        "OMI": "????????????",

        "AWZ": "??????????",

        "IHR": "?????????? ??????",

        "IIL": "??????????",

        "BBL": "????????????",

        "BJB": "????????????",

        "BXR": "????",

        "BND": "???????? ????????",

        "BDH": "???????? ????????",

        "MRX": "???????? ????????????",

        "IAQ": "????????????",

        "BUZ": "??????????",

        "XBJ": "????????????",

        "BSM": "???????? ??????",

        "PFQ": "???????? ????????",

        "TBZ": "??????????",

        "TCX": "??????",

        "IKA": "??????????",

        "THR": "??????????",

        "TEW": "??????????",

        "KHK": "?????????? ????????",

        "SXI": "?????????? ????????",

        "KIH": "?????????? ??????",

        "JYR": "??????????",

        "ZBR": "????????????",

        "KHA": "????????",

        "KHD": "?????? ????????",

        "KHY": "??????",

        "DEF": "??????????",

        "RZR": "??????????",

        "RAS": "??????",

        "RJN": "??????????????",

        "ACZ": "????????",

        "ZAH": "????????????",

        "JWN": "??????????",

        "SRY": "????????",

        "AFZ": "????????????",

        "CKT": "????????",

        "SDG": "??????????",

        "ACP": "????????",

        "SYJ": "????????????",

        "CQD": "?????? ??????",

        "SYZ": "??????????",

        "PGU": "????????????",

        "FAZ": "????????",

        "GZW": "??????????",

        "GSM": "??????",

        "GCH": "??????????????",

        "GBT": "??????????",

        "LRR": "??????",

        "LFM": "??????????",

        "LVP": "??????????",

        "MHD": "????????",

        "NUJ": "????????",

        "NSH": "??????????",

        "IFH": "??????",

        "HDM": "??????????",

        "HDR": "??????????????",

        "KNR": "????????????",

        "KER": "??????????",

        "KSH": "????????????????",

        "KLM": "??????????",

        "YES": "??????????",

        "AZD": "??????"

    }

    # serialize data obj as a JSON stream
    data = json.dumps(data)
    response = HttpResponse(data, content_type='application/json charset=utf-8')

    return response
