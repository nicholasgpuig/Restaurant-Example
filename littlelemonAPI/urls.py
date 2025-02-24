from django.urls import include, path
from rest_framework import routers
from littlelemonAPI.views import SingleMenuItemViewSet, MenuItemViewSet

router = routers.DefaultRouter()
router.register('menu', MenuItemViewSet)

urlpatterns = [
    path('menu/<int:pk>/', SingleMenuItemViewSet.as_view()),
    path('menu/', MenuItemViewSet.as_view()),
]