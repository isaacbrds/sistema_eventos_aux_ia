from django.urls import path
from . import views
urlpatterns = [
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/<int:id>', views.detalhe_evento, name='detalhe_evento')
]