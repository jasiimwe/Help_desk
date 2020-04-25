from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment
from account.models import Account
from .forms import EquipmentCreateForm

# Create your views here.
def equipment_view(request):
    equipment = Equipment.objects.all()    
    return render(request, 'equipment/show_equipment.html', {'equipment': equipment})

def equipment_create(request):
    context = {}
    if request.POST:
        form = EquipmentCreateForm(request.POST)
        if form.is_valid():
            eq = form.save(commit=False)
            eq.user = request.user
            form.save()
            return redirect('show_equipment')
        else:
            context['equipment_form'] = form
    else:
        form = EquipmentCreateForm()
        context['equipment_form'] = form
    return render(request, 'equipment/create_equipment.html', context)

def edit_equipment(request, pk):
    context = {}
    equipment = get_object_or_404(Equipment, pk=pk)

    if request.method == "POST":
        form = EquipmentCreateForm(request.POST, instance=equipment)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.user = request.user
            equipment.save()
            
            return redirect('show_equipment')
            #context['success_message'] = "Updated Successfully"
    else:
        form = EquipmentCreateForm(instance=equipment)
        context['edit_form'] = form    
        
    return render(request, 'equipment/edit_equipment.html', context)

def equipment_detail_view(request, pk):
    context = {}
    equipment = get_object_or_404(Equipment, pk=pk)
    context['equipment_detail'] = equipment

    return render(request, 'equipment/equipment_detail.html', context)