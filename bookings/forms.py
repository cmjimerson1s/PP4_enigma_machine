from django import forms
from .models import Reservation, GameTime, Room

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'customer_name',
            'customer_email',
            'customer_phone',
            'comment',
        ]

        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),
            'customer_email': forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}),
            'customer_phone': forms.TextInput(attrs={'placeholder': 'Phone Number: +## #########'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Comment or Request'}),
        }

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields['customer_name'].widget.attrs.update({'autofocus': True})
                self.fields['customer_email'].widget.attrs.update({'autofocus': True})
                self.fields['customer_phone'].widget.attrs.update({'autofocus': True})
                self.fields['comment'].widget.attrs.update({'autofocus': True})

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('customer_name')
            emails = cleaned_data.get('customer_email')
            phone = cleaned_data.get('customer_phone')
            message = cleaned_data.get('comment')

            if not name:
                self.add_error('name', 'Please enter your name.')
            if not emails:
                self.add_error('emails', 'Please enter your email.')
            if not phone:
                self.add_error('phone', 'Please enter your phone number.')
            if not message:
                self.add_error('message', 'Please enter your message.')

            return cleaned_data        