from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError


class Reservation(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14, validators=[validate_phone_number])
    price = models.IntegerField()
    date = models.DateField(auto_created=False)
    time_slot = models.CharField(max_length=5)
    comment = models.TextField(max_length=300, default='')
    user_id = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.time_slot} + {self.date}"


#Model validators below
def validate_phone_number(value):
    if not value.startswith("+"):
        raise ValidationError("Phone number must start with '+'")
    if not value[1:].isdigit():
        raise ValidationError("Phone number must contain only digits after '+'")
    if len(value) != 13:
        raise ValidationError("Phone number must be in the format '+## ##########'")
