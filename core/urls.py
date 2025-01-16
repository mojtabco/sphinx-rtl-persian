from django.urls import path
from core import views

urlpatterns = [
    path('', views.index_View, name='index'),
    path('elements/', views.elements_View, name='elements'),
    path('multimedia/', views.multimedia_View, name='multimedia'),
    path('page/', views.page_View, name='page'),
    path('page1/', views.page1_View, name='page1'),
    path('page2/', views.page2_View, name='page2'),
    path('page3/', views.page3_View, name='page3'),
]