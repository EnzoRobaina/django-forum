from django.urls import path
from . import views

urlpatterns = [
    path('', views.log, name="login_page"),
    path('logout/', views.logout_view, name="logout_page"),
    path('registrar/', views.registrar, name="registrar"),
    #path('registrar/', views.Registrar.as_view(), name="registrar"),
    path('forum/', views.forum, name="forum"),
    path('forum/<str:discussao_titulo>/', views.discussao, name="discussao" ),
    path('forum/<str:discussao_titulo>/topico/<int:topico_id>/', views.topico, name="topico"),
    path('forum/<str:discussao_titulo>/criar_topico/', views.criar_topico, name="criar_topico"),
]