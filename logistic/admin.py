from django.contrib import admin
from logistic.models import Client, Package, Sheet, ItemSheet, Report

class ClientAdmin(admin.ModelAdmin):
  list_display=("name")
  list_filter=("number_phone")
  search_fields=("name")

class SheetAdmin(admin.ModelAdmin):
  list_filter = ("date")
  date_hierachy = ("date")


admin.site.register(Client, ClientAdmin)
admin.site.register(Package)
admin.site.register(Sheet)
admin.site.register(ItemSheet)
admin.site.register(Report)
