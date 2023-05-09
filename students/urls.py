from django.urls import path
from . import views

urlpatterns = [

# path('', views.main, name='main'),
path('', views.students, name='students'),
path('details/<int:id>', views.details, name='details'),

path('testing/', views.testing, name='testing'),
path('link1/', views.link1, name='link1'),
path('link2/', views.link2, name='link2'),
path('link3/', views.link3, name='link3'),
path('search/', views.index, name='index'),

]