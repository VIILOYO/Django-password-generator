from django.urls import path
from .views import password, index, info


urlpatterns = [
    path('', index, name='index'),
    path('password', password, name='password'),
    path('info', info, name='info'),
]
