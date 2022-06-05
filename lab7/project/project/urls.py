from django.contrib import admin
from django.urls import path, include
from showplace import views
from category import views

from showplace.views import ShowplaceViewSet
from category.views import CategoryViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("api/showplaces", ShowplaceViewSet, basename="showplaces")
router.register("api/category", CategoryViewSet, basename="category")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('index', views.index, name='home'),  
]

urlpatterns += router.urls