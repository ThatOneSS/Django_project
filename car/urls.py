from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, RegionViewSet, CompanyViewSet

router=DefaultRouter()
router.register("car",CarViewSet,basename="car")
router.register("region",RegionViewSet,basename="region")
router.register("company",CompanyViewSet,basename="company")
urlpatterns = [
    path("",include(router.urls)),
]