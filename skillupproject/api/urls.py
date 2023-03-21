from rest_framework import routers
from .views import SampleViewSet

router = routers.DefaultRouter()
router.register(r'samples', SampleViewSet)