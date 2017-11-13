from django.contrib import admin
from .models import Item

# Register your models here.

admin.site.register(Item, list_display=['item_type', 'item_name', 'item_price'])
