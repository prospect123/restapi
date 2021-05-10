from rest_framework.pagination import LimitOffsetPagination



class mylimitoffsetpagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3