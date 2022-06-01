from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='home'),   
    path('profile', views.profile, name='profile'), 
    path('showplaces/', views.showplaces, name='showplaces'),    
    path('showplaces/<int:showplace_id>/', views.showplaces, name='showplaces'),
    path('admin/', admin.site.urls),
]
