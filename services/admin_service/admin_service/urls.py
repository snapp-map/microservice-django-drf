from django.urls import path
from .views import AdminUsersView, AdminProductsView, AdminOrdersView, AdminPaymentsView
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
    path("api/admin/users/", AdminUsersView.as_view(), name="admin-users"),
    path("api/admin/products/", AdminProductsView.as_view(), name="admin-products"),
    path("api/admin/orders/", AdminOrdersView.as_view(), name="admin-orders"),
    path("api/admin/payments/", AdminPaymentsView.as_view(), name="admin-payments"),
]
