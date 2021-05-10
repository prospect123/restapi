from django.urls import path
from .import views

urlpatterns = [
    path('limit-offfset-pagination/', views.Limitoff_pagination.as_view(), name='user_list'),
    path('cursor-pagination/', views.cursor_pagination.as_view(), name='user_list'),
    path('pagenumber-pagination/', views.pagenumber_pagination.as_view(), name='user_list'),
]