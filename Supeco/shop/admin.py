from django.contrib import admin

from shop.models import Section, Product, Order

admin.site.register(Section)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    # actions_on_bottom = True
    # actions_on_top = False
    list_per_page = 4
    search_fields = ('title',)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
        'phone', 'email', 'status'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
