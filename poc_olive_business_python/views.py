# poc_olive_business_python/views.py

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse

from .models import Product

def getProducts(request):    
    products = [Product("001", "Apple", 5, True), 
                Product("002", "Banana", 4.3, False),
                Product("003", "Orange", 3.2, True)]
        
    data = serialize("json", products)

    return HttpResponse(data, content_type="application/json")