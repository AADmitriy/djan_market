import os
from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import ValidationError
from django.conf import settings

from PIL import Image
from .models import Product


def frontpage(request):
    return render(request, 'market/frontpage.html')

def contacts(request):
    return render(request, 'market/contacts.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'market/products.html', {'products': products})

def food_products(request):
    """
    return the same page as product func,
    but with form which only contain products with type 'food'
    """
    food_products = Product.objects.filter(type='food')
    return render(request, 'market/products.html', {'products': food_products})

def drinks_products(request):
    """
    return the same page as product func,
    but with form which only contain products with type 'drinks'
    """
    drinks_products = Product.objects.filter(type='drinks')
    return render(request, 'market/products.html', {'products': drinks_products})

def add_product(request):
    if request.user.is_staff:  # check whether user have rights to access this page
        if request.method == 'POST':
            form = request.POST.dict()  # Retrieve data from form and convert it to dict
            products = Product.objects.all()

            name = form['name']
            errors = [] 
            if name.lower() in [p.name.lower() for p in products]:  # check that the name is not unique 
                # if true return empty form with error data
                errors.append('Name is already taken!')
                return render(request, 'market/add_product.html', {'errors': errors})
            
            img_name = request.FILES['image'].name
            if img_name.split('.')[-1] not in ['jpg', 'jpeg', 'png']:  # check whether file is not supported
                # if true return empty form with error data
                errors.append('File extension is not supported!')
                return render(request, 'market/add_product.html', {'errors': errors})
            
            
            # Create new file name that unique in DB
            new_img_name = name + '_' + img_name  

            # Build relative path to img
            path_to_new_img = os.path.join('market', 'images', 'discounts', new_img_name)

            # Build full path to img
            full_path_to_new_img = os.path.join(settings.STATICFILES_DIRS[0], path_to_new_img)


            img_dict = request.FILES.dict()  # Retrieve file data from form and convert it to dict
           
            with img_dict['image'].open('r') as f:  # Open img from form in read mode
                im1 = Image.open(f)
                im1.save(full_path_to_new_img)  # Copy and upload file to server
            
            
            cost = form['cost']
            amount = form['amount']
            type = form['type']
            p = Product(name=name, path_to_img=path_to_new_img, cost=cost, amount=amount, type=type)  # Creates new product
            p.save()
            
            return redirect(success)
        
        # if method is not POST return page with empty form
        return render(request, 'market/add_product.html')
    
    else:
        raise Http404

def success(request):
    if request.user.is_staff: # check whether user have rights to access this page
        return render(request, 'market/success.html')
    else:
        raise Http404
