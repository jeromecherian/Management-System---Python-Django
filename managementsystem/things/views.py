from django.shortcuts import render,redirect
from . models import Product, Category 
# Create your views here.
def home(request):
    return render(request,'home.html')

def category(request):
    c= Category.objects.all()
    return render(request,'category.html',{"d":c})

def addcategory(request):
    if request.method=="POST":
        obj=Category()
        obj.name=request.POST["name"]
        obj.save()
        return redirect("home")

def product(request):
    a = Product.objects.all()
    n = Category.objects.all() 
    return render(request, 'product.html', {'b': a, 'n': n})
    
def addproduct(request):
    if request.method=="POST":
        obj=Product()
        obj.name=request.POST.get("name")
        obj.description=request.POST.get("description")
        obj.price=request.POST.get("price")
        obj.brand=request.POST.get("brand")
        obj.category=Category.objects.get(id=request.POST.get("category"))
        obj.save()
        return redirect("home")
    n=Category.objects.all()
    return redirect(request,"addproduct.html",{"n":n})

def delete_category(request,id):
    i = Category.objects.get (id=id)
    i.delete()
    return category(request)





def delete_product(request,id):
    i = Product.objects.get (id=id)
    i.delete()
    return product(request)

def productedit(request, id):
    e = Product.objects.get(id=id)
    n = Category.objects.all()
    return render(request, "productedit.html", {"f": e, "n": n})

def updateproduct(request,id):
     if request.method=="POST":
        obj = Product.objects.get(id=id)
        obj.name=request.POST["name"] 
        obj.description=request.POST["description"]
        obj.price=request.POST["price"]
        obj.brand=request.POST["brand"]
        obj.category = Category.objects.get(id=request.POST["category"])
        obj.save()
        return redirect("product")


     