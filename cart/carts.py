from decimal import Decimal
from django.conf import settings
from store.models import Item

class Cart(object):
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)

		if not cart:
			#save an empty cart in the session
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart


	def add(self, product, quantity=0, update_quantity=False):
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity':0, 'price':str(product.item_price)}
		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save()

	def save(self):
		self.session[settings.CART_SESSION_ID] = self.cart
		self.session.modified = True

	def remove(self, product):
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()
	def __iter__(self):
		product_ids = self.cart.keys()
		products = Item.objects.filter(id_in=product_ids)
		for product in products:
			self.cart[str(product.id)]['product'] = product

			for item in self.cart.values():
				item['item_price'] = Decimal(item['item_price'])
				item['total_price'] = item['item_price' * item['quantity']]
				yield item
	def __len__(self):
		"""
		Counts all the items in the cart
		"""
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_cost(self):
		return sum(Decimal(item['item_price']) * item['quantity'] for item in self.cart.values())




	def clear(self):
		#remove cart from session
		del self.session[settings.CART_SESSION_ID]
		self.session.modified  = True

