from django.db import models
from datetime import datetime

# Create your models here.

class Item(models.Model):
	item_type = models.CharField(max_length=255)
	item_name = models.CharField(max_length=255)
	item_cost = models.IntegerField()
	item_description = models.TextField(max_length=5024)
	item_image = models.ImageField(upload_to='items')
	date_added = models.DateField(default=datetime.now)

	def __str__(self):
		return self.item_type + ' - ' + self.item_name