from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers
from .views import PaperViewSet

router = routers.DefaultRouter()
router.register('papers', PaperViewSet)

urlpatterns = [
    # /people/list
    path('list', views.PeopleView.as_view(), name='people_list'),
    path('', include(router.urls)),
    path('test', views.TestView.as_view())
]
