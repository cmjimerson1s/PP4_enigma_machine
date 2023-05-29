from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError


class Reservation(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    player_number = models.IntegerField(null=True)
    price = models.IntegerField()
    date = models.DateField(auto_created=False)
    time_slot = models.ForeignKey(
        "GameTime", on_delete=models.CASCADE, related_name="time_slot", null=True
    )
    room_choice = models.ForeignKey(
        "Room", on_delete=models.CASCADE, related_name="room_choice", null=True
    )
    comment = models.TextField(max_length=300, default="", blank=True)
    user_id = models.IntegerField(default=0)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date} + {self.time_slot} + {self.room_choice}"


class Room(models.Model):
    room_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    short_room_description = models.CharField(
        max_length=250, unique=True, null=True
        )
    room_description = models.TextField()
    small_image = CloudinaryField("small image", default="placeholder")
    detail_image = CloudinaryField("large image", default="placeholder")

    class Meta:
        ordering = ["room_name"]

    def __str__(self):
        return self.room_name


class GameTime(models.Model):
    GAME_SLOTS = [
        ("00:00", "00:00"),
        ("02:00", "02:00"),
        ("04:00", "04:00"),
        ("06:00", "06:00"),
        ("08:00", "08:00"),
        ("10:00", "10:00"),
        ("12:00", "12:00"),
        ("14:00", "14:00"),
        ("16:00", "16:00"),
        ("18:00", "18:00"),
        ("20:00", "20:00"),
        ("22:00", "22:00"),
    ]
    game_slot = models.CharField(max_length=5, choices=GAME_SLOTS)

    class Meta:
        ordering = ["game_slot"]

    def clean(self):
        # See if there's already a GameTime instance with the same game_slot
        if GameTime.objects.filter(game_slot=self.game_slot).exists():
            raise ValidationError("A slot already exists for this time.")

    def __str__(self):
        return self.game_slot
