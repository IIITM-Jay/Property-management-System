from django.contrib import admin

# Register your models here.
from .models import Asset


# Register your models here.

from .forms import AssetForm

class AssetAdmin(admin.ModelAdmin):
   list_display = ["Property_type","Property_name","location","Establishment_date","timestamp"]
   form = AssetForm
   list_filter = ['Property_type', 'Property_name','location']
   search_fields =  ['Property_type', 'Property_name','location']


admin.site.register(Asset,AssetAdmin)

