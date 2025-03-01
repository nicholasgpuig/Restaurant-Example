from django.urls import include, path
from rest_framework import routers
from littlelemonAPI import views

router = routers.DefaultRouter()
router.register('menu', views.MenuItemViewSet)

urlpatterns = [
    path('menu/<int:pk>/', views.SingleMenuItemViewSet.as_view()),
    path('menu/', views.MenuItemViewSet.as_view()),
    path('reservations/', views.ReservationItemViewSet.as_view()),
    path('reservations/<int:pk>/', views.SingleReservationItemViewSet.as_view()),
]