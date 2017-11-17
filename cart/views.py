from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from store.models import Item
from .carts import Cart
from .forms import CartAddProductForm

# Create your views here.
@login_required
def cart_detail(request):
	print('details atleast working')

	cart = Cart(request)
	if cart:
		print(cart)
	else:
		print('NO items in cart')


	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity':item['quantity'],'update':True })
		print('details cart')
	return render(request, 'cart/detail.html', {'cart':cart})

@login_required
@require_POST
def cart_add(request, item_id):
	cart = Cart(request)
	print('nnkjkhgyf')
	# product = Item.objects.get(id=item_id)
	product = get_object_or_404(Item, id=item_id)
	# print(product.item_price)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
		print(str(product) + ' added')

	return redirect('cart:cart_detail')

@login_required
def cart_remove(request, item_id):
	cart = Cart(request)
	product = get_object_or_404(Item, id=item_id)
	cart.remove(product)
	return redirect('cart:cart_detail')

def product_detail(request, id, slug):
	product = get_object_or_404(Item, id=id, slug=slug, available=True)
	cart_product_form = CartAddProductForm()
	return render(request, '../store/item_detail.html', {'product':product, 'cart_product_form':cart_product_form})
