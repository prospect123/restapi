from django.urls import path
from .import views

urlpatterns = [
    path('generic-create/', views.USERCreateView.as_view(), name='user_create'),
    path('generic-list/', views.USERListView.as_view(), name='user_list'),
    path('generic/<int:pk>/detail/', views.USERRetrieveView.as_view(), name='user_retrieve'),
    path('generic/<int:pk>/delete/', views.USERDeleteView.as_view(), name='user_delete'),
    path('generic/<int:pk>/update/', views.USERUpdateView.as_view(), name='user_update'),
    path('generic-list-create/', views.userListCreateView.as_view(), name='movie_list_create'),
    path('generic/<int:pk>/retrieve-update/', views.userRetrieveUpdateView.as_view(), name='user_retrieve_update'),
    path('generic/<int:pk>/retrieve-destroy/', views.userRetrieveDestroyView.as_view(), name='user_retrieve_destroy'),
    path('generic/<int:pk>/retrieve-update-destroy/', views.userRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy'),
]