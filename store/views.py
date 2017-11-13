from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Item

from cart.forms import CartAddProductForm
# Create your views here.

class ItemListView(ListView):
	model = Item
	template_name = 'store/index.html'
	context_object_name = 'items'

class ItemDetailView(DetailView):
	model = Item
	template_name = 'store/item_detail.html'
	context_object_name = 'item_detail'



def product_detail(request, id):
	product = get_object_or_404(Item, id=id)
	cart_product_form = CartAddProductForm()
	return render(request, 'store/item_detail.html', {'product':product, 'cart_product_form':cart_product_form})