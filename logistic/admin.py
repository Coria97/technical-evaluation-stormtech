from django.contrib import admin
from logistic.models import Client, Package, Sheet, ItemSheet, Report

class PackageInline(admin.TabularInline):
  model = Package
  fields = ["tracking", "weight", "height", "status", "package_type"]

  # optional: make the inline read-only
  readonly_fields =  ["tracking", "weight", "height", "status", "package_type"]
  can_delete = False
  max_num = 0
  extra = 0
  show_change_link = True
class PackageAdmin(admin.ModelAdmin):
  list_display=("tracking", "weight", "height", "status", "package_type", 'client',"client_details")


  def client_details(self, obj):
    if obj.client:
        return f"{obj.client.name} | {obj.client.email} | {obj.client.phone_number} | {obj.client.street} {obj.client.street_number}"
    else:
        return None

class ClientAdmin(admin.ModelAdmin):
  list_display=("name", "email", "street", "street_number", "phone_number")
  list_filter=("street", "street_number")
  search_fields=["email"]
  inlines = [PackageInline] 
  
#class SheetAdmin(admin.ModelAdmin):
#  list_filter = ("date")
#  date_hierachy = ("date")

admin.site.register(Client, ClientAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Sheet)
admin.site.register(ItemSheet)
admin.site.register(Report)
