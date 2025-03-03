from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Django ATS API",
        default_version="v1",
        description="API documentation for the django ats project",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
