from django.shortcuts import render
from registerformapp.forms import NewuserForm

# Create your views here.
def index(request):
    return render(request,'registerformapp/index.html')

def users(request):
    form=NewuserForm()

    if(request.method=='POST'):
        form=NewuserForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)

    return render(request,'registerformapp/user.html',{'form':form})
