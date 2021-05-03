from django.shortcuts import render,get_object_or_404,redirect
from .models import Product 
from .forms import ProductForm
# Create your views here.


#product create form view
def product_create_view(request):
    form=ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form': form
    }
    return render(request,'products/product_create.html',context)

#update form view
def product_update_view(request,id=id):
    obj = get_object_or_404(Product,id=id)
    form = ProductForm(request.POST or None,instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product',  obj.id)
    context={
        'form': form
    }
    return render(request,'products/product_create.html',context)


#form delete view
def product_delete_view(request,id):
    obj= get_object_or_404(Product,id=id)
    print(obj.title)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context={
        'obj':obj
    }
    return render(request,'products/product_delete.html',context)

#list view
def product_list_view(request):
    products=Product.objects.all()
    context={
        'products': products
    }
    return render(request,'products/product_list.html',context)


#product detail view
def product_detail_view(request,id):
    product=get_object_or_404(Product,id=id)
    context={
        'product':product
    }
    return render(request,'products/product_detail.html',context)