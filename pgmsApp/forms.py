from django import forms
from pgmsApp.models import Occupant,ElectricityBill

class OccupantRegistrationForm(forms.ModelForm):
    class Meta:
        model = Occupant
        fields = '__all__'
    
class ElectricityBillForm(forms.ModelForm):
    class Meta:
        model = ElectricityBill
        fields = '__all__'