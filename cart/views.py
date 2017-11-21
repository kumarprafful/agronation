from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from store.models import Item
from .models import Cart, CartItem
from .forms import CartAddProductForm
from .carts import add, remove, get_total_price, clear

# Create your views here.
@login_required
def cart_detail(request):
	quantity_form = {}
	cart = get_object_or_404(Cart,user=request.user)
	cart_items = CartItem.objects.filter(cart=cart)
	tp = get_total_price(cart)
	for item in cart_items:
		quantity_form = CartAddProductForm(initial={'quantity':item.quantity,'update':True })
	
	return render(request, 'cart/detail.html', {'cart_items':cart_items, 'update_quantity_form':quantity_form, 'total_price':tp})

@login_required
@require_POST
def cart_add(request, item_id):
	cart = get_object_or_404(Cart,user=request.user)
	# product = Item.objects.get(id=item_id)
	product = get_object_or_404(Item, id=item_id)
	# print(product.item_price)
	form = CartAddProductForm(request.POST)
	print('ajsna')
	if form.is_valid():
		cd = form.cleaned_data
		add(cart=cart, product=product, quantity=cd['quantity'], update_quantity=cd['update'])
		print(str(product) + ' added')

	return redirect('cart:cart_detail')

@login_required
def cart_remove(request, item_id):
	cart = get_object_or_404(Cart,user=request.user)
	product = get_object_or_404(Item, id=item_id)
	remove(cart=cart,product=product)
	return redirect('cart:cart_detail')

# def product_detail(request, id, slug):
# 	product = get_object_or_404(Item, id=id, slug=slug, available=True)
# 	cart_product_form = CartAddProductForm()
# 	return render(request, '../store/item_detail.html', {'product':product, 'cart_product_form':cart_product_form})
