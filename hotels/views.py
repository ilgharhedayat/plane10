from django.shortcuts import render

import json

import requests

from django.views.generic import View


# Create your views here.
class HotelView(View):
    def get(self, request):
        response = requests.get('https://api.vhotel.ir/api/V4/hotels', auth=('admin', "iEol5iBJjFCRKIBA"))
        hotel_list = json.loads(response.content)
        return render(request, 'hotels/list.html', {'hotels_list': hotel_list})


# parsa
# https://api.vhotel.ir/api/V4/cities

class HotelSearchView(View):
    def get(self, request):
        response = requests.post(f'https://api.vhotel.ir/api/V4/availabilityByCity/',
                                 auth=('admin', "iEol5iBJjFCRKIBA"),
                                 body=({request.GET.get('cityId')}, {request.GET.get('from')}, {request.GET.get('to')}))
        hotel_list = json.loads(response.content)
        return render(request, 'hotels/list.html', {'hotels_list': hotel_list})
