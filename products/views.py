from django.http import HttpResponse ,JsonResponse
from .models import Product


def home(request):
    return HttpResponse('<H1 > Hello Kendall </H1>')

def api_products01(request):
    products= Product.objects.all()
    data = []

    for product in products:
        data.append({
            'id':product.id,
            'name':product.name,
            'descrition':product.description,
            'price':product.price,
            'stock':product.stock,
            'asset':product.asset
        })

    return JsonResponse({'products':data})



def api_products_all(request):
    products = Product.objects.values(
        'id','name','description','price','stock','asset'
    )
    return JsonResponse({'products':list(products)})

###There we started with DRF ###


from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from products.serializers import ProductSerializer
##from products.models import Producto## Its over
@api_view(['GET','POST']) 

def api_products(request):
    if request.method == 'GET':
        products= Product.objects.all().order_by('id')
        serializer = ProductSerializer(products,many=True)
        return  Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()

            return Response(serializer.data,
                            status=status.HTTP_201_CREATED
                            )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )
@api_view(['GET','PUT','PATCH','DELETE'])

def details_products(request,pk):
    try :
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:

        return Response(
            {'error':'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    if request.method in ['PUT','PATCH']:
        serializer = ProductSerializer(
            product,
            data = request.data,
            partial =(request.method == 'PATCH')
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    if request.method == 'DELETE':
        product.delete()
        return Response (status= status.HTTP_204_NO_CONTENT)



