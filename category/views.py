from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all() # Consulta todos los registros[cite: 3]
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)