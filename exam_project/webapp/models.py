from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.category_name


class Advert(models.Model):
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, related_name='advert')
    picture = models.ImageField(null=True, blank=True, upload_to='pictures')
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=3000, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='advert')
    is_moderated = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        permissions = (("can_view_new_ads", "Can view new ads"),
                       ("can_view_rejected_ads", "Can view rejected ads"))


# Create your models here.
