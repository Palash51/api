from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from rest_framework import generics
from test1.serializer import CarsSerializer,Transaction_infoSerializer,Parking_lotSerializer,User_infoSerializer
from models import Cars,Transaction_info,Parking_lot,User_info
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

def home(request):
	context = {'latest_question_list': "latest_question_list"}
	return render(request, 'index.html', context)

class Detail(generics.ListCreateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	
	queryset = Cars.objects.all()
	serializer_class = CarsSerializer


class Transaction(generics.ListCreateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	
	queryset = Transaction_info.objects.all()
	serializer_class = Transaction_infoSerializer

class Parking(generics.ListCreateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	
	queryset = Parking_lot.objects.all()
	serializer_class = Parking_lotSerializer

class GetUser(generics.ListCreateAPIView):
	"""
	wgatfghkp
	"""
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	
	queryset = User_info.objects.all()
	serializer_class = User_infoSerializer


class GetUserHistory(generics.ListCreateAPIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	def post(self,request,fromat=None):
		username = request.POST.get('username')
		# return Transaction_info.objects.filter(username=username)
		return Response(Transaction_infoSerializer(Transaction_info.objects.filter(username=username),many=True).data)




