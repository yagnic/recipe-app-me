from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurants import views


router = DefaultRouter()
router.register('restaurants', views.RestaurantViewSet)


app_name = 'restaurants'

urlpatterns = [
    path('', include(router.urls))
]
