from django import forms
from .models import Reservation, GameTime, Room
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'customer_name',
            'customer_email',
            'comment',
        ]


        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),
            'customer_email': forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Comment or Request'}),
        }


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['customer_name'].initial = f"{user.first_name} {user.last_name}"
        if user:
            self.fields['customer_email'].initial = user.email
        

