from django.contrib import admin
from logistic.models import Client, Package, Sheet, ItemSheet, Report
from logistic.utils import PackageType,PackageStatus

def mark_packages_as_distributed(modeladmin, request, queryset):
    for sheet in queryset:
      item_sheets = ItemSheet.objects.filter(sheet=sheet)
      for item_sheet in item_sheets:
        item_sheet.package.status = PackageStatus.DISTRIBUTION
        item_sheet.package.save()

mark_packages_as_distributed.short_description = "Marcar paquetes como en distribución"

class PackageInline(admin.TabularInline):
  model = Package
  readonly_fields =  ["package_type"]
  fields = ["tracking", "weight", "height", "status", "package_type"]
  can_delete = False
  extra = 0

class PackageAdmin(admin.ModelAdmin):
  readonly_fields =  ["package_type"]
  list_display = ("tracking", "weight", "height", "status", "package_type", "client_details")
  search_fields = ["tracking"]
  list_filter = ["package_type", "status"]

  def client_details(self, obj):
    if obj.client:
        return f"{obj.client.name} | {obj.client.email} | {obj.client.phone_number} | {obj.client.street} {obj.client.street_number}"
    else:
        return None
      
  def save_model(self, request, obj, form, change):
    for weight_limit, package_type in PackageType.choices():
      if obj.weight <= weight_limit:
          obj.package_type = package_type
          break
    super().save_model(request, obj, form, change)


class ClientAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "street", "street_number", "phone_number")
  list_filter = ("street", "street_number")
  search_fields = ["email"]
  inlines = [PackageInline]
  
class ReportAdmin(admin.ModelAdmin):
  readonly_fields = ["title", "status", "description", "get_item_sheet"]
  list_display = ("title", "status", "description")
  list_filter = ["status"]
  
  def get_item_sheet(self, obj):
    if obj.failure_reasons:
        return obj.failure_reasons.position
    return None

  get_item_sheet.short_description = "Item Sheet"
  
  def has_add_permission(self, request):
    return False

  def has_delete_permission(self, request, obj=None):
    return False
  
  def has_change_permission(self, request, obj=None):
    return False

class ItemSheetInline(admin.TabularInline):
    model = ItemSheet
    extra = 0

class SheetAdmin(admin.ModelAdmin):
  list_display = ("sheet_number", "date")
  list_filter = ["date"]
  date_hierachy = ("date")
  inlines = [ItemSheetInline]
  actions = [mark_packages_as_distributed]

class ItemSheetAdmin(admin.ModelAdmin):
   readonly_fields = ["failure_reasons"]
   list_display = ("position", "sheet", "package")

admin.site.register(Client, ClientAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Sheet, SheetAdmin)
admin.site.register(ItemSheet, ItemSheetAdmin)
admin.site.register(Report,ReportAdmin)
