from django.shortcuts import render
from .models import user
from django.http import HttpResponse
from django.contrib import messages
from users.form import userform
# Create your views here.
def home(request):
    user_a = user()
    if request.method == 'POST':
        form = userform(request.POST)

        if form.is_valid():
            user_a = form
            user_a.save()
        messages.success(request,'Saved sucessfully')
    

    form1 = userform()
    return render(request,'home.html',{'form':form1})

def viewall(request):
    data = user.objects.all()
    users = {"user_number":data}
    return render(request,"viewall.html",users)