
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta
from django.http import JsonResponse
from .models import Food
from django.db.models import Q
from .forms import CategoryForm, FoodItemForm
from django.db import models
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    foods = Food.objects.all()
    return render(request, 'inventory/home.html', {'foods': foods})
 
def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoodItemForm()
    return render(request, 'inventory/add_food_item.html', {'form': form})

def get_inventory(request):
    foods = list(Food.objects.values())
    return JsonResponse(foods, safe=False)

def edit_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        # Handle form submission, update food object
        food.name = request.POST.get('name')
        food.quantity = request.POST.get('quantity')
        # unit = models.CharField(max_length=10, default='unit')
        food.unit=request.POST.get('unit', default='packs')
        food.category = request.POST.get('category')
        food.ideal_quantity = request.POST.get('ideal_quantity')
        food.best_before = request.POST.get('best_before')
        food.save()
        return redirect('home')
    return render(request, 'inventory/edit_food.html', {'food': food})

def delete_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    food.delete()
    return redirect('home')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'inventory/add_category.html', {'form': form})

def stock_overview(request):
    foods = Food.objects.all()
    for food in foods:
        food.status = "Overstocked" if food.quantity > food.ideal_quantity else "Understocked" if food.quantity < food.ideal_quantity else "Optimal"
    return render(request, 'inventory/stock_overview.html', {'foods': foods})

def expiring_soon(request):
    today = date.today()
    next_week = today + timedelta(days=7)
    foods = Food.objects.filter(best_before__range=(today, next_week)).order_by('best_before')
    
    for food in foods:
        food.days_left = (food.best_before - today).days  # Custom attribute for display
    
    return render(request, 'inventory/expiring_soon.html', {'foods': foods})



def search_food(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
    if query:
        foods = Food.objects.filter(name__icontains=query)
    else:
        foods = Food.objects.all()  # If no query, return all foods

    return render(request, 'inventory/search_results.html', {'foods': foods, 'query': query})


def shopping_list(request):
    foods = Food.objects.all()
    items_to_buy = []

    for food in foods:
        if food.quantity < food.ideal_quantity:
            items_to_buy.append({
                'name': food.name,
                'needed_quantity': food.ideal_quantity - food.quantity,
                # 'current_quantity': food.quantity,
                # 'ideal_quantity': food.ideal_quantity,
                # 'category': food.category,
            })

    return render(request, 'inventory/shopping_list.html', {'items_to_buy': items_to_buy})
