from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(regex=r"^(\+996),?\s?\d{9}$", message="Phone number must be entered in the format: '+996 000 000 000.")


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='profile',
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.user.username


# Create your models here.
