from django.db import models, IntegrityError
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import AbstractUser, Permission, Group
import random
# Create your models here.

class Account(AbstractUser):
    account_number = models.PositiveIntegerField(unique=True)
    zip_code = models.CharField(max_length=15)
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='account_user_permissions'
    )

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='accounts_groups'
    )
    
    def get_api_url(self):
        return reverse("api_accounts", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.account_number:
            while True:
                random_number = random.randint(0000, 9999)
                self.account_number = str(random_number)
                try:
                    super(Account, self,).save(*args, **kwargs)
                except IntegrityError:
                    continue
                break
        else:
            super(Account, self).save(*args, **kwargs)


class Pet(models.Model):
    pet_number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    owner = models.ForeignKey(
        Account, 
        related_name="pets", 
        on_delete=models.CASCADE
        )

    def save(self, *args, **kwargs):
        if not self.pet_number:
            while True:
                random_number = random.randint(00000, 99999)
                self.pet_number = str(random_number)
                try:
                    super(Pet, self,).save(*args, **kwargs)
                except IntegrityError:
                    continue
                break
        else:
            super(Pet, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

