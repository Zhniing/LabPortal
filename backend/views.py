from django.shortcuts import render
from django.views.generic import View
from django.http.response import JsonResponse
from rest_framework import viewsets
from .models import Paper, Test
from .serializers import PaperSerializer, TestSerializer

# Create your views here.

class PeopleView(View):

    def get(self, request):
        return JsonResponse([{'name':'zhangsan'}, {'name':'lisi'}, {'name':'wangwu'}], safe=False)


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class TestView(View):
     
     def get(self, request):
        qs = Test.objects.all()
        
        ser = TestSerializer(qs, many=True)

        return JsonResponse(ser.data, safe=False)
