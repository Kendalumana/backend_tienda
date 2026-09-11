
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from users.serializers import UserSerializer
from .models import User

@api_view(['GET','POST']) 

def api_users(request):
    if request.method == 'GET':
        users= User.objects.all().order_by('id')
        serializer = UserSerializer(users,many=True)
        return  Response(serializer.data)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
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

def details_users(request,pk):
    try :
        user = User.objects.get(pk=pk)

    except User.DoesNotExist:

        return Response(
            {'error':'User not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method in ['PUT','PATCH']:
        serializer = UserSerializer(
            user,
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
        user.delete()
        return Response (status= status.HTTP_204_NO_CONTENT)



