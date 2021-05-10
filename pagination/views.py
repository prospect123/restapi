from rest_framework.generics import (ListAPIView,)
from .serializers import *
from .limit_offset_pagination import *
from .cursor_pagination import *
from .page_number_pagination import *

class Limitoff_pagination(ListAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer
    pagination_class = mylimitoffsetpagination

class cursor_pagination(ListAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer
    pagination_class = cursors_pagination

class pagenumber_pagination(ListAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer
    pagination_class = pagenumberpagination

