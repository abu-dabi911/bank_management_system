from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, related_name="customer_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customer_permissions", blank=True)

    def __str__(self):
        return self.username

class Account(models.Model):

    ACCOUNT_TYPES = [
        ('Savings', 'Savings'),   # Сберегательный счет
        ('Checking', 'Checking'), # Расчетный счет
    ]

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name='accounts')
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.account_type} - {self.customer.username}"
