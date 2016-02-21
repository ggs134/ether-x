from django.contrib import admin

# Register your models here.

from .models import EthAccount, Transaction
admin.site.register(EthAccount)
admin.site.register(Transaction)