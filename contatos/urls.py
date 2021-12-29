from django.urls import path, include
from . import views
from rest_framework import routers
from contatos.views import ContatoViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Agenda",
        default_version="v1",
        description="Documentação de endpoints do Agenda",
    ),
    public=False,
    permission_classes=[permissions.IsAuthenticated],
)

router = routers.DefaultRouter()
router.register(r'Contato', ContatoViewSet)

urlpatterns = [
    path('', views.agenda, name='agenda'),
    path('', views.busca, name='busca'),
    path('<int:contato_id>/', views.ver_contato, name='ver_contato'),
    path('api/', include(router.urls)),

    # Documentação de endpoints Swagger e Redoc
    path(
        "docs/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "docs/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

