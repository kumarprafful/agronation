from django.contrib import admin
from .models import Item, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['item_type', 'slug']
	prepopulated_fields = {'slug':('item_type',)}
admin.site.register(Category, CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
	list_display = ['item_name', 'slug', 'item_price','stock','available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['item_price', 'stock', 'available']
	prepopulated_fields = {'slug':('item_name',)}

admin.site.register(Item, ItemAdmin)
