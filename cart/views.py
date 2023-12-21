from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Category
from .forms import ProductForm, AccountCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "index.html",{'products':products})

def product_details(request, id):
        product = get_object_or_404(Product, pk=id)
        context = {"product": product}
        return render(request, 'details.html', context)

def delete_product(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return redirect('cart:index')
      
 
def edit_product(request, id):
    pi = Product.objects.get(pk=id)
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        form = ProductForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('cart:index')
                
    else:
        form = ProductForm(instance=pi)        
    return render(request, 'edit_product.html', {'form':form})
   
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  
        if form.is_valid():
            company_name= form.cleaned_data['company_name']
            product_name= form.cleaned_data['product_name']
            category_names = form.cleaned_data['category']
            brand = form.cleaned_data['brand']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            description = form.cleaned_data['description'] # Assuming category is a multiple select field
            post = Product( company_name=company_name, product_name=product_name, brand=brand, price=price, quantity=quantity,  description=description)
            post.save()
            
            for category_name in category_names:
                    category = get_object_or_404(Category, name=category_name)
                    post.category.add(category)
            form = ProductForm()  # Clear the form
            return redirect("cart:index")
    else:
            form = ProductForm()            
    return render(request, "add_product.html", {'form': form})   

def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page
            return redirect('cart:login')
            
    else:
        form = AccountCreationForm()
    return render(request, 'register.html', {'form': form})    
   
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        # validate email and password
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("cart:index")
    else:
        form = LoginForm()
    context = {"form": form} 
    return render(request, "login.html", context)

    
def logout_request(request):
    logout(request)
    return redirect("cart:login")    