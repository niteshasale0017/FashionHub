from django.shortcuts import render
from django.http import HttpResponse 
from product.models import Shirt,Pant,Shoe
# Create your views here.
def demo(request):
    if request.method == 'POST':
        size = request.POST['size']
        quantity = request.POST['quantity']
        print(size)
        print(quantity)
        print('******************')
        return render(request,'order/demo.html',{'size':size,'quantity':quantity})
def size(request):
    if request.method =='POST':
        size_quantity = ''
        result = ''
        product_id = request.POST['product_id']
        print(product_id)
        size = request.POST['size']
        print(size)
        print(product_id)
        if size == 'size_m':
            size_quantity = Shirt.objects.get(id=product_id)
            result = size_quantity.size_m
        elif size == 'size_l':
            size_quantity = Shirt.objects.get(id=product_id)
            result = size_quantity.size_l
        elif size == 'size_xl':
            size_quantity = Shirt.objects.get(id=product_id)
            result = size_quantity.size_xl
        elif size == 'size_28':
            size_quantity = Pant.objects.get(id=product_id)
            result = size_quantity.size_28
        elif size == 'size_30':
            size_quantity = Pant.objects.get(id=product_id)
            result = size_quantity.size_30
        elif size == 'size_32':
            size_quantity = Pant.objects.get(id=product_id)
            result = size_quantity.size_32
        elif size == 'size_34':
            size_quantity = Pant.objects.get(id=product_id)
            result = size_quantity.size_34
        elif size == 'size_7':
            size_quantity = Shoe.objects.get(id=product_id)
            result = size_quantity.size_7
        elif size == 'size_8':
            size_quantity = Shoe.objects.get(id=product_id)
            result = size_quantity.size_8            
        elif size == 'size_9':
            size_quantity = Shoe.objects.get(id=product_id)
            result = size_quantity.size_9
        else:
            size_quantity = Shoe.objects.get(id=product_id,)
            result = size_quantity.size_10
        print(result)
        return HttpResponse(result)
def cartdetail(request):
    cart = request.session.get('cart')
    for i in cart:
        if 'Shirt' == i:
            shirt_ids = []
            for j in cart[i]:
                shirt_ids.append(j)
            shirt = Shirt()
            shirt_data = shirt.get_shirt_data(shirt_ids)
           
        elif 'Pant' == i:
            pant_ids = []
            for j in cart[i]:
                pant_ids.append(j)
            pant = Pant()
            pant_data = pant.get_pant_data(pant_ids)
                
        else:
            shoe_ids = []
            for j in cart[i]:
                shoe_ids.append(j)
            shoe = Shoe()
            shoe_data = shoe.get_shoe_data(shoe_ids)
            
    value = {}
    value['shirt_data'] = shirt_data
    value['pant_data'] = pant_data
    value['shoe_data'] = shoe_data

    

            
    return render(request,'order/cartdetail.html',value)