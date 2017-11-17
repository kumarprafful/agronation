from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Item, Category
from cart.forms import CartAddProductForm
# Create your views here.

def item_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	items = Item.objects.all()
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		items = items.filter(category=category)
	return render(request, 'store/index.html', {'category':category, 'categories':categories, 'items':items})


def item_detail(request, category_slug, slug):
	category = get_object_or_404(Category, slug=category_slug)
	item = get_object_or_404(Item, slug=slug)
	return render(request, 'store/item_detail.html', {'item':item})








# class ItemListView(ListView):
# 	model = Item
# 	template_name = 'store/index.html'
# 	context_object_name = 'items'

# class ItemDetailView(DetailView):
# 	model = Item
# 	template_name = 'store/item_detail.html'
# 	context_object_name = 'item_detail'

# def product_detail(request, id):
# 	product = get_object_or_404(Item, id=id)
# 	cart_product_form = CartAddProductForm()
# 	return render(request, 'store/item_detail.html', {'product':product, 'cart_product_form':cart_product_form})