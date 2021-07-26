from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('BackendAccount', views.BackendAccountView)
router.register('Class', views.ClassView)
router.register('Manager', views.ManagerView)
router.register('FrontAccount', views.FrontAccountView)

urlpatterns = [
    path('', include(router.urls)),
]
