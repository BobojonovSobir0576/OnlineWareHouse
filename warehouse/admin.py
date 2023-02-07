from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from warehouse.models import *


@admin.register(ProductBarcode)
class ProductBarcodeAdmin(ImportExportModelAdmin):
    list_display =['id','name_product']
    search_fields =['name_product']
    
admin.site.register(Scanproduct)
    