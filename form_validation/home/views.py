from django.shortcuts import render,HttpResponse,redirect
from .forms import EmployeeForm
# Create your views here.
def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                return HttpResponse('Data send successfully')
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})
                        
        