from django.shortcuts import render, redirect
from snadhanapp.models import customer_details
from snadhanapp.forms import customer_detailsForm

def retrieve_view(request):
    customer_detail = customer_details.objects.all()
    return render(request,'snadhanapp/index.html', {'customer_detail':customer_detail})
def create_view(request):
    form = customer_detailsForm()
    if request.method == 'POST':
        form = customer_detailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create')
    return render(request,'snadhanapp/create.html',{'form': form})

def delete_view(request,id):
    customer_detail = customer_details.objects.get(id=id)
    customer_detail.delete()
    return redirect('/retrieve')
# Create your views here.
