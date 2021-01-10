from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Category, Company, ProductSize, ProductSite, Comment, Image


#admin.register() decorator
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content')
    list_filter = ('category',)

# add model to admin panel
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSize)
admin.site.register(ProductSite)
admin.site.register(Comment)
admin.site.register(Image)

#remove default model from admin
admin.site.unregister(Group)

#change the title of admin panel
admin.site.site_header = "Product Review Admin"


