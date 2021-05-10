from rest_framework.pagination import CursorPagination

class cursors_pagination(CursorPagination):
    page_size = 3
    ordering = 'mobile_no'