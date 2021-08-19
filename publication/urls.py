from django.urls.conf import include, path
from rest_framework import routers
from .views import AuthorViewSet, PaperViewSet
from . import views

router = routers.DefaultRouter()

router.register('authors', AuthorViewSet)
router.register('papers', PaperViewSet)

urlpatterns = [
    # /publ/api
    path('', include(router.urls)),
    path('home', views.HomeView.as_view())
]
