from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=300, null=False, blank=False)


class Advert(models.Model):
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, related_name='advert')
    picture = models.ImageField(null=True, blank=True, upload_to='pictures')
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=3000, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='advert')
    is_moderated = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField(null=True, blank=True)


# Create your models here.
