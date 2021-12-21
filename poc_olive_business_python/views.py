# poc_olive_business_python/views.py

import json

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer

class ProductViews(APIView):
    keycloak_roles = {'GET': ['ROLE_ADMIN']}

    def get(self, request):        
        products = [Product("001", "Apple", 5, True).as_json(), 
                    Product("002", "Banana", 4.3, False).as_json(),
                    Product("003", "Orange", 3.2, True).as_json()]

        return Response(data=products, content_type="application/json", status=status.HTTP_200_OK)