from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET'])
def get_book(request):
   book_obj = Book.objects.all()
   serializer = bookserializer(book_obj,many=True)
   return Response({'status':200 , 'payload': serializer.data})







@api_view(['GET'])
def home(request):
    studend_objs = Student.objects.all()
    serializer = StudentSerializer(studend_objs, many= True)
    return Response({'payload':serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)
    if not serializer.is_valid():
        return Response({'error':serializer.errors})
    serializer.save()
    return Response({'state' : 200 ,'payload':serializer.data})

@api_view(['PUT'])
def update_student(request,id):
  try:
     student_obj  = Student.objects.get(id = id)
     serializer = StudentSerializer(student_obj , data = request.data , partial= True)
     if not serializer.is_valid():
        return Response({'error':serializer.errors})
     serializer.save()
     return Response({'state' : 200 ,'payload':serializer.data})
  except Exception as e:
    return Response({'status':403,'message':'invalide id '})

@api_view(['DELETE'])
def delete_student(request,id):
    try:   
        student_obj  = Student.objects.get(id = id)
        student_obj.delete()
        return Response({'status':200,'message':'delete'})

    except Exception as e:
       return Response({'status':403,'message':'invalide id '})
     
class registerUser(APIView):
        def POST(self,request):
            serializer = UserSerializer(data = request.data)
            if not serializer.is_valid():
                return Response({'status':403, 'paylod':serializer.error})
            serializer.save()
            user = User.objects.get(username =serializers.data["username"] )
            token_obj , _ = Token.objects.get_or_create(user=user)
            return Response({'statu':200,'payload':serializer.data,'token':str(token_obj)})
        