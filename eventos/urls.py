from django.urls import path
from . import views
urlpatterns = [
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/<int:id>/', views.detalhe_evento, name='detalhe_evento'),
    path('eventos/<int:id>/participar/', views.participar_evento, name='participar_evento'),
    path('palestras/<int:id>/', views.detalhe_palestra, name='detalhe_palestra'),
    path('palestras/<int:id>/inscrever', views.inscrever_palestra, name='inscrever_palestra'),
    path('palestrantes/<int:id>/', views.detalhe_palestrante, name='detalhe_palestrante'),
    path('participantes/perfil/', views.perfil_participante, name='perfil_participante'),
]