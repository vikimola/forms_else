from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=255,
                            validators=[MinLengthValidator(2, "Min 2 chars required")]
                            )

    def __str__(self):
        return self.name


class Cat(models.Model):
    nickname = models.CharField(max_length=255,
                                validators=[MinLengthValidator(2, "Min 2 chars required")]
                                )
    weight = models.DecimalField(decimal_places=1, max_digits=3, validators=[MinValueValidator(0)])
    foods = models.CharField(max_length=5000, blank=True)
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname
