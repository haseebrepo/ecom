from django.contrib import admin
from .models import Product
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Broadcast a notification when a new product is added
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "product_updates",  # Group name
            {
                "type": "product_notification",
                "message": f"New product added: {obj.name}"
            }
        )
