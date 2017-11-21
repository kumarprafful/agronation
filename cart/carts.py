from .models import Cart, CartItem
from store.models import Item 
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

def add(cart,product,quantity=1,update_quantity=False):
	try:
		item = CartItem.objects.get(cart=cart,product=product)

	except ObjectDoesNotExist:
		item = CartItem.objects.create(product=product,cart=cart,quantity=0,price=product.item_price,total_price=0)

	if update_quantity:
		item.quantity = quantity

	else:
		item.quantity += quantity

	item.total_price = item.price * item.quantity
	item.save()


def remove(cart,product):
	item = get_object_or_404(CartItem,cart=cart,product=product)
	item.delete()

def get_total_price(cart):
	items = CartItem.objects.filter(cart=cart)
	tp = 0
	for item in items:
		tp += item.price * item.quantity
	return tp

def clear(cart):
	CartItem.objects.filter(cart=cart).delete()

