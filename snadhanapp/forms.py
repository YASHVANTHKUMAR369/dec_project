from django import forms
from snadhanapp.models import customer_details
class customer_detailsForm(forms.ModelForm):
   class Meta:
        model = customer_details
        fields = '__all__'
        
        
#Data --> information
#Meta data --> Data about Data
