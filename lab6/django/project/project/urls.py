from django.contrib import admin
from django.urls import path, include
from showplace import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('showplace.urls')),
]