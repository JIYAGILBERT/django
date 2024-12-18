from django.shortcuts import render, redirect

from .models import *
def index(request):
        if request.POST:
            todo123=request.POST.get("todo1")
            obj=Todoitem(title=todo123)
            obj.save()
            
            return redirect(index)
        data=Todoitem.objects.all()
        return render(request,"index.html",{"feeds":data})
    # Create your views here.
