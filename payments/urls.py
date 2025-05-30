from rest_framework import routers
from django.urls import path, include

from payments.views import PaymentViewSet

app_name = "payments"

router = routers.DefaultRouter()
router.register("payments", PaymentViewSet, basename="payments")

urlpatterns = [path("", include(router.urls))]
