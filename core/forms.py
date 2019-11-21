from django import forms
from django.db.models import BooleanField
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
import re
from allauth.account.forms import SignupForm
import time 


ADDRESS_CHOICES = (
    ('Lamachaur', 'Lamachaur'),
    ('Chipledhunga', 'Chipledhunga'),
    ('Mahendrapool', 'Mahendrapool'),
    ('Newroad', 'Newroad'),
    ('Nayabazar', 'Nayabazar'),
    ('Sabhagriha', 'Sabhagriha'),
    ('PrithviChowk', 'PrithviChowk'),
    ('Birauta', 'Birauta'),
    ('Begnas', 'Begnas'),
    ('LakeSide', 'LakeSide'),
)


PAYMENT_CHOICES = (
    ('CashOnDelivery', 'CashOnDelivery'),
    ('Others', 'Others')
)

TIME_CHOICES = (
    ('7PM TODAY', '7PM TODAY'),
    ('6AM TOMORROW', '6AM TOMORROW'),
    ('7PM TOMORROW', '7PM TOMORROW'),
)

class CheckoutForm(forms.Form):
    address = forms.CharField(widget=forms.Select(choices=ADDRESS_CHOICES), max_length=100)
    phonenumber = forms.CharField(max_length=100)
    paymentoption = forms.CharField(max_length=100, widget=forms.Select(choices=PAYMENT_CHOICES))
    deliveryoption = forms.CharField(max_length=30, widget=forms.Select(choices=TIME_CHOICES))

    def clean_phonenumber(self):
        number = self.cleaned_data['phonenumber']
        if re.match('9[87]{1}[654210]{1}\d{7}$', number):
            return number
        else:
            raise forms.ValidationError('Please provide a valid phone number.')

    def clean_deliveryoption(self):
        deliveryoption = self.cleaned_data['deliveryoption']
        t = time.localtime()
        print(t.tm_hour + t.tm_min / 60 + t.tm_sec / 3600)
        if deliveryoption == '7PM TODAY':
            deliveryoption_in_int = int(deliveryoption[0])
            if ( deliveryoption_in_int + 12 ) > ( t.tm_hour + t.tm_min / 60 + t.tm_sec / 3600 ):
                return deliveryoption
            else:
                raise forms.ValidationError('You r ahead of your time.')
        else:
            return deliveryoption