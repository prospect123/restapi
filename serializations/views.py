from django.shortcuts import render
from serializations.models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework import viewsets


class hyperlinkserliModelViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_classs = hyperlinkedSerializer

def user_detail(request,pk):
    use = user.objects.get(id=pk)
    serializer = userSerializer(use)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='json/application')
