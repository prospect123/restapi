from django.urls import path
from .import views

urlpatterns = [
    path('mixins-list/', views.userlist.as_view(), name='user_list'),
    path('mixins-create/', views.usercreate.as_view(), name='user_create'),
    path('mixins-retrive/<int:pk>/', views.userretrive.as_view(), name='user_retrive'),
    path('mixins-update/<int:pk>/', views.userupdate.as_view(), name='user_update'),
    path('mixins-destory/<int:pk>/', views.userdestory.as_view(), name='user_destory'),

]