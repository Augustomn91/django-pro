from django.urls import path, include
from . import views
from rest_framework import routers
from contatos.views import ContatoViewSet

router = routers.DefaultRouter()
router.register(r'Contato', ContatoViewSet)

urlpatterns = [
    path('', views.agenda, name='agenda'),
    path('', views.busca, name='busca'),
    path('<int:contato_id>/', views.ver_contato, name='ver_contato'),
    path('api/', include(router.urls)),
]
