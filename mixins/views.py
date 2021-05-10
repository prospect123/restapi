from .models import *
from .serializers import userSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class userlist(GenericAPIView,ListModelMixin):
    queryset = user.objects.all()
    serializer_class = userSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class usercreate(GenericAPIView,CreateModelMixin):
    queryset = user.objects.all()
    serializer_class = userSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class userretrive(GenericAPIView,RetrieveModelMixin):
    queryset = user.objects.all()
    serializer_class = userSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class userupdate(GenericAPIView,UpdateModelMixin):
    queryset = user.objects.all()
    serializer_class = userSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class userdestory(GenericAPIView,DestroyModelMixin):
    queryset = user.objects.all()
    serializer_class = userSerializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)