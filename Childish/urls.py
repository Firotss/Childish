from django.urls import include, path
from django.views.generic import TemplateView
from API import views
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.contrib import admin
router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/stats/price/<str:date_start>:<str:date_end>', views.price_list),
    path('api/stats/count/<str:date_start>:<str:date_end>', views.count_list),
    path('openapi/', get_schema_view(
        title="Childish Project",
    ), name='openapi-schema'),
    path('admin/', admin.site.urls)
]
