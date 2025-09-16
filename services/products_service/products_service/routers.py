from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, reduce_stock
from django.urls import path

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")

# internal reduce-stock endpoint
reduce_stock_urlpatterns = [
    path("products/<int:pk>/reduce-stock/", reduce_stock, name="reduce-stock"),
]

urlpatterns = router.urls + reduce_stock_urlpatterns
