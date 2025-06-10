from django import forms
from .models import Food
from .models import Category
class FoodItemForm(forms.ModelForm):
    best_before = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Food
        fields = ['name', 'category', 'quantity', 'unit', 'best_before','ideal_quantity']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'ideal_quantity']