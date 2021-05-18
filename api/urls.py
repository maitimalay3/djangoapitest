from django.urls import path
from django.conf.urls import url
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="WindApp API",
      default_version='v1',
      description="WindApp Backend APIs",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('wind_test', views.WindTest.as_view(), name='wind_test'),
    url(r'^get_result/(?P<task_id>[\w.+_-]+)/$',   views.GetResult.as_view(), name='get_result'),
    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]