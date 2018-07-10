from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name="index"),
    path('', views.main, name="main"),
    #path('topico/<int:>', views.topico, name="topico"),
    path('topico/<int:topico_id>/', views.topico, name='topico'),
    path('criar_topico/', views.criar_topico, name="criar_topico"),
]