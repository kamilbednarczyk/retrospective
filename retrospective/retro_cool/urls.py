from django.urls import path

from retro_cool import views

urlpatterns = [
    path('', views.main, name='retro_list'),
    path('add', views.add, name='retro_add'),
    path('view', views.view, name='retro_view')
]