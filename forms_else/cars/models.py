from django.core import validators
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
# class Cars(models.Model):
#     nickname = models.CharField(max_length=255)
#     make = models.CharField(max_length=255, blank=True)
#     mileage = models.IntegerField()
#     comments = models.TextField(blank=True)

class Make(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="Enter a make (pl. Ford):",
        validators=[MinLengthValidator(2)]
    )

    def __str__(self):
        return self.name


class Auto(models.Model):
    nickname = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(2)]
    )
    make = models.ForeignKey("Make", on_delete=models.CASCADE)
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.nickname
