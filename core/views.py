from django.shortcuts import render
from .models import ContactUs
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import ContactUsForm


# Create your views here.
class ContactUsView(SuccessMessageMixin, CreateView):
    model = ContactUs
    success_url = reverse_lazy('passengers:home')
    success_message = 'پیام شما با موفقیت ثبت شد'
    form_class = ContactUsForm
    template_name = 'core/contact_us.html'
