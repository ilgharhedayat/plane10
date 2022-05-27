from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email',
            'phone_number',
            'title',
            'text',
        )
        labels = {
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'title': 'موضوع',
            'text': 'متن',
        }
