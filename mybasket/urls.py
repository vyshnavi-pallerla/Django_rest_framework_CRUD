from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns = [
    path('',views.products),
    path('<int:id>', views.product_detail),
    path('schema', SpectacularAPIView.as_view(), name = 'schema'),
    path('schema/docs', SpectacularSwaggerView.as_view(url_name = 'schema')),
]

urlpatterns = format_suffix_patterns(urlpatterns)