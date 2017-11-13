from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from store.models import Item
from .carts import Cart
from .forms import CartAddProductForm

# Create your views here.
@login_required
def cart_detail(request):
	cart = Cart(request)
	return render(request, 'cart/detail.html', {'cart':cart})

@login_required
@require_POST
def cart_add(request, item_id):
	cart = Cart(request)
	product = get_object_or_404(Item, id=item_id)
	# print(product)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
	return redirect('cart:cart_detail')

@login_required
def cart_remove(request, item_id):
	cart = Cart(request)
	product = get_object_or_404(Item, id=item_id)
	cart.remove(product)
	return redirect('cart:cart_detail')

