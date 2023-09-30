from django.urls import path
from . import views
urlpatterns = [
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/<int:id>/', views.detalhe_evento, name='detalhe_evento'),
    path('palestrantes/<int:id>/', views.detalhe_palestrante, name='detalhe_palestrante'),
]