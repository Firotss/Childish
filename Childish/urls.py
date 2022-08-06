from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from API import views

router = routers.DefaultRouter()
router.register(r'api/stats', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('openapi/', get_schema_view(
        title="Childish Project",
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui')
]
