from django.db import router
from django.urls import path, include
from .views import DemoViewSet, TestView
from rest_framework import routers

router = routers.DefaultRouter()

# /brain_seg/demo
router.register('demo', DemoViewSet)

urlpatterns = [
    # /brain_seg/
    path('', include(router.urls)),
    # path('demo', DemoViewSet.as_view()),
    path('test', TestView.as_view())
]
