from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
	item_type = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True, db_index=True)

	class Meta:
		ordering = ('item_type',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_absolute_url(self):
		return reverse('store:item_list_by_category', args=[self.slug])

	def __str__(self):
		return self.item_type

class Item(models.Model):
	category = models.ForeignKey(Category, related_name='item')
	item_name = models.CharField(max_length=255, db_index=True)
	item_image = models.ImageField(upload_to='items')
	slug = models.SlugField(db_index=True, max_length=255)
	item_price = models.IntegerField()
	item_description = models.TextField(blank=True)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)    

	class Meta:
		ordering = ('item_name',)
		index_together = (('id', 'slug'),) 

	def get_absolute_url(self):
		return reverse('store:item_detail', args=[self.category.slug, self.slug])


	def __str__(self):
		return self.category.item_type + ' - ' + self.item_name