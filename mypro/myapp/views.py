from django.shortcuts import render, redirect

from .models import *
def index(request):
        if request.POST:
            todo123=request.POST.get("todo1")
            print(todo123)
            obj=Todoitem(title=todo123)
            obj.save()
            
            return redirect(index)
        data=Todoitem.objects.all()
        return render(request,"index.html",{"feeds":data})
    
def delete_g(request,id):
    feeds=Todoitem.objects.filter(pk=id)
    feeds.delete()
    return redirect(index)

def edit_g(request,pk):
    if request.method=="POST":
        todo123=request.POST.get("todo1")
        Todoitem.objects.filter(pk=pk).update(title=todo123)
        return redirect('index')
    else:
        data=Todoitem.objects.get(pk=pk)
        return render(request,'index.html',{'data1':data})
    
    # Create your views here.
