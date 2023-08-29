from django.shortcuts import render,redirect
from pgmsApp.models import Occupant,ElectricityBill
from pgmsApp.forms import OccupantRegistrationForm,ElectricityBillForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.

class OccupantListView(ListView):
    model = Occupant
    #occupant_list
    

class OccupantCreateView(CreateView):
    model = Occupant
    success_url = reverse_lazy('index')
    fields = ('name','occupation','roomType','entryDate')
    #occupant_form
    
 
class OccupantUpdateView(UpdateView):
    model = Occupant
    success_url = reverse_lazy('index')
    fields = ('name','occupation','roomType','entryDate')
    

class OccupantDeleteView(DeleteView):
    model = Occupant
    success_url = reverse_lazy('index')
     
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Username or Password is incorrect')
    return render(request,'pgmsApp/login.html')
    
@login_required
@permission_required('pgmsApp.addData_pgmsdb')
def AddDate(request,**kwargs):
    form=ElectricityBillForm()
    occupant=Occupant.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=ElectricityBillForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'pgmsApp/electricitybill_form.html',{'form':form,'occupant':occupant})

def logoutOccupant(request):
    return render(request,'pgmsApp/logout.html')

@login_required
def calculate(request,**kwargs):
    data = ElectricityBill.objects.filter(occupant_id=kwargs['pk'])
    result = []
    for entry in data:
        if entry.days>1:
            bill= entry.days *100
            billing1 = ElectricityBill()
            billing2 = Occupant()
            billing1.entry=billing2.entryDate
        
            billing1.days=bill
            result.append(billing1)
        result.append(entry)
    return render(request,'pgmsApp/generatebill.html',{'data':result})
            
    
    