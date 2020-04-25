from django import forms
from .models import Equipment

class EquipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('equipment_type','serial_number','station','user_assesment',
        'current_condition','recommendation','current_location','delivered_by','phone_number','status')

    def clean_serial_number(self):
        serial_number = self.cleaned_data.get('serial_number')
        try:
            equipment = Equipment.objects.exclude(pk=self.instance.pk).get(serial_number=serial_number)
        except Equipment.DoesNotExist:
            return serial_number
        raise forms.ValidationError('Serial number "%s" already exists' % equipment)
    
    