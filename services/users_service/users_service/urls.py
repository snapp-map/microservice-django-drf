from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .routers import router
from .views import MyTokenObtainPairView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
    path("admin/", admin.site.urls),
    path(
        "api/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # JWT login
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # JWT refresh
    path("api/", include(router.urls)),
]
