from django import forms
from .models import Asset

 
class AssetForm(forms.ModelForm):
   class Meta:
      model = Asset
      fields = ['Property_type', 'Property_name','location','Establishment_date']
   
   
class AssetSearchForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['Property_type', 'location','export_to_CSV']

