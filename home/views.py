from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PeopleSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class RegisterUser(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            return Response({
            'status':False,'message': serializer.errors
            },status.HTTP_400_BAD_REQUEST)
    
        serializer.save()
        user = User.objects.get(username = serializer.data['username'], password=serializer.data['password'])
        token_obj , _ = Token.objects.get_or_create(user=user)
        return Response({'status': True, 'payload' : serializer.data, 'token' : str(token_obj) ,'message':'your data is stored'},status.HTTP_201_CREATED)








# class LoginAPI(APIView):

#    def post(self, request):
#         data=request.data
#         serializer=LoginSerializer(data=data)
#         if not serializer.is_valid():
#             return Response({
#             'status':False,'message': serializer.errors
#             },status.HTTP_400_BAD_REQUEST)
    
#         serializer.save()
#         user= authenticate(username= serializer.data['username'],password=serializer.data['password'])
#         if not user:
#             return Response({
#             'status':False,'message': 'invalid Credentials'
#             },status.HTTP_400_BAD_REQUEST)
    

#         token , _ = Token.objects.get_or_create(user=user)
#         return Response({'status': True, 'payload' : serializer.data, 'message':str(token)},status.HTTP_201_CREATED)



# class RegisterAPI(APIView):
#    def post(self, request):
#         data=request.data
#         serializer=RegisterSerializer(data=data)

#         if not serializer.is_valid():
#             return Response({
#                 'status':False,'message': serializer.errors
#             },status.HTTP_400_BAD_REQUEST)
        
#         serializer.save()

#         return Response({
#             'status': True, 'message':'User Created'
#         },status.HTTP_201_CREATED)

    

class PersonAPI(APIView):
    def get(self,request):
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def put(self,request):
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def patch(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message' : 'person deleted'})

@api_view(['GET'])
def index(request):
    courses = {
        'course_name' : 'python',
        'learn' : ['flask', 'django', 'fastapi', 'tornado'],
        'course_provider' : 'scaler'
    }
    return Response(courses)

# @api_view(['POST'])
# def login(request):
#     data = request.data
#     serializer = LoginSerializer(data = data)
#     if serializer.is_valid():
#         data = serializer.validated_data
#         return Response({'message' : 'success'})
#     else:
#         return Response(serializer.errors)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message' : 'person deleted'})
    

class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith = search)
        serializer = PeopleSerializer(queryset, many=True)
        return Response({'status' : 200, 'data' : serializer.data}, status=status.HTTP_204_NO_CONTENT)
