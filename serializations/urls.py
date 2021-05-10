from django.urls import path,include
from serializations import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hyperlinkser',views.hyperlinkserliModelViewSet,basename='hyperlinkserlizer')


urlpatterns = [
    path('serializer/<int:pk>/', views.user_detail, name='serializer_list'),
    path('admin/',admin.site.urls),
    path('hyperlinkser/',include(router.urls)),
]