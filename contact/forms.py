from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            "inquiry_name",
            "inquiry_email",
            "phone_number",
            "inquiry_message",
        )
        widgets = {
            "inquiry_name": forms.TextInput(
                attrs={
                    "class": "form-control", "placeholder": "Name",
                    "id": 'name'
                }
            ),
            "inquiry_email": forms.EmailInput(
                attrs={
                    "class": "form-control", "placeholder": "Email",
                    "id": 'email'
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Phone Number",
                    "id": 'phone'
                }
            ),
            "inquiry_message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "What is your Question?",
                    "id": 'message'
                }
            ),
        }
