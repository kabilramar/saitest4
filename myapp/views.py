from unicodedata import name

from django import db
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

from .models import Student
# insert operation
def index(request):
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        try:
            db=Student.objects.create(name=name,age=age)
            db.save()
            print("SAVED")
            return redirect('select')
        except:
            print("error")
    return render(request,"index.html")

def edit (request,id):
    db=Student.objects.get(id=id)
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        try:
            db.name=name
            db.age=age
            db.save()
            print("updated")
            return redirect("select")
        except:
            print("error")
    return render(request,"edit.html",{"data":db})


def delete(request,id):
    db=Student.objects.get(id=id)
    db.delete()
    print("deleted")
    return redirect('select')

def select(request):
    data=Student.objects.all()
    return render(request,"select.htm",{"data":data})
