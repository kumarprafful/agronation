from django.db import models
from store.models import Item 
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
	user = models.ForeignKey(User)
	items = models.ManyToManyField(Item,through='CartItem',blank=True)

	def __str__(self):
		return self.user.username

class CartItem(models.Model):
	product = models.ForeignKey(Item)
	cart = models.ForeignKey(Cart)
	image = models.ImageField(upload_to='cart/products', default='noimage.png')
	quantity = models.PositiveIntegerField()
	price = models.PositiveIntegerField()
	total_price = models.PositiveIntegerField(null=True)

	def __str__(self):
		return self.product.item_name + '-' + self.cart.user.username



