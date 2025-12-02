# finance/models.py
from django.db import models

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('income', 'Кіріс'),
        ('expense', 'Шығыс'),
    ]
    
    title = models.CharField("Сипаттама", max_length=100)
    amount = models.DecimalField("Сома", max_digits=10, decimal_places=2)
    transaction_type = models.CharField("Түрі", max_length=10, choices=TYPE_CHOICES)
    date = models.DateField("Күні", auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.amount} ({self.transaction_type})"
