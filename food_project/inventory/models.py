from django.db import models
from datetime import date

UNIT_CHOICES = [
    ('kg', 'Kilograms'),
    ('g', 'Grams'),
    ('l', 'Litres'),
    ('ml', 'Millilitres'),
    ('packs', 'Packs'),
]

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ideal_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='packs')
    best_before = models.DateField(default=date.today)
    ideal_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
from django.db import models
from datetime import date

UNIT_CHOICES = [
    ('kg', 'Kilograms'),
    ('g', 'Grams'),
    ('l', 'Litres'),s
    ('ml', 'Millilitres'),
    ('packs', 'Packs'),
]

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ideal_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='packs')
    best_before = models.DateField(default=date.today)
    ideal_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
