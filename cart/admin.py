from django.contrib import admin
from .models import Cart,OrderPlaced,Orders, Payment

admin.site.register(Orders)
admin.site.register(Cart)
admin.site.register(OrderPlaced)
admin.site.register(Payment)


