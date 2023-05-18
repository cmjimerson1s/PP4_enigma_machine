from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError


#Model validators below

def validate_phone_number(value):
    if not value.startswith("+"):
        raise ValidationError("Phone number must start with '+'")
    if not value[1:].isdigit():
        raise ValidationError("Phone number must contain only digits after '+'")
    if len(value) != 12:
        raise ValidationError("Phone number must be in the format '+###########'")


class Reservation(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=14, validators=[validate_phone_number])
    price = models.IntegerField()
    date = models.DateField(auto_created=False)
    time_slot = models.ForeignKey('GameTime', on_delete=models.CASCADE, related_name="time_slot", null=True)
    room_choice = models.ForeignKey('Room', on_delete=models.CASCADE, related_name="room_choice", null=True)
    comment = models.TextField(max_length=300, default='')
    user_id = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} + {self.time_slot} + {self.room_choice}"


class Room(models.Model):
    room_name = models.CharField(max_length=200, unique=True)
    room_description = models.TextField()
    blog_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['room_name']

    def __str__(self):
        return self.room_name


class GameTime(models.Model):
    GAME_SLOTS = [
        ('00:00','00:00'),
        ('02:00','02:00'),
        ('04:00','04:00'),
        ('06:00','06:00'),
        ('08:00','08:00'),
        ('10:00','10:00'),
        ('12:00','12:00'),
        ('14:00','14:00'),
        ('16:00','16:00'),
        ('18:00','18:00'),
        ('20:00','20:00'),
        ('22:00','22:00'),
    ]
    game_slot = models.CharField(max_length=5, choices=GAME_SLOTS)

    class Meta:
        ordering = ['game_slot']

    def clean(self):
        # Check if there is already a GameTime instance with the same game_slot value
        if GameTime.objects.filter(game_slot=self.game_slot).exists():
            raise ValidationError("A slot already exists for this time.")

    def __str__(self):
        return self.game_slot
