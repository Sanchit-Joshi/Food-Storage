from datetime import date
from django.test import TestCase
from .models import Category
from .forms import FoodItemForm

class FoodItemFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fruits", ideal_quantity=10)

    def test_food_form_valid_data(self):
        form = FoodItemForm(data={
            'name': 'Apple',
            'category': self.category.id,
            'quantity': 5,
            'unit': 'kg',
            'best_before': date.today(),
            'ideal_quantity': 10
        })
        self.assertTrue(form.is_valid())

    def test_food_form_multiple_invalid_fields(self):
        form = FoodItemForm(data={
            'name': '',                         # Missing name
            'category': self.category.id,
            'quantity': '',                     # Missing quantity
            'unit': '',                         # Missing unit
            'best_before': 'not-a-date',        # Invalid date
            'ideal_quantity': ''                # Missing ideal quantity
        })

        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('quantity', form.errors)
        self.assertIn('unit', form.errors)
        self.assertIn('best_before', form.errors)
        self.assertIn('ideal_quantity', form.errors)
