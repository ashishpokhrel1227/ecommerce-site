from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Item, Order, Order, CheckOut
from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json

from core.models import Item, OrderItem, Order, CheckOut

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'ordered_date', 'ordered')
    ordering = ('-start_date', )

    def changelist_view(self, request, extra_context=None):

        char_data = (
            Order.objects.annotate(date=TruncDay('start_date')).values('date')
            .annotate(y=Count('user'))
            .order_by('date')
            .filter(ordered=True)
        )

        as_json = json.dumps(list(char_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {'char_data': as_json}

        return super().changelist_view(request, extra_context=extra_context)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price')
admin.site.register(Item, ItemAdmin)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'ordered', 'delievered', 'deliveryoption', 'ordered_date')
admin.site.register(OrderItem, OrderItemAdmin)

class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('user','deliveryoption')
admin.site.register(CheckOut, BillingAddressAdmin)

admin.site.unregister(Group)

