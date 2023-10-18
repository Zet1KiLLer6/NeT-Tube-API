from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register('genre', GenreModelViewSet)
router.register('year', YearModelViewSet)
router.register('author', AuthorModelViewSet)
router.register('country', CountryModelViewSet)
router.register('publication', PublicationNameModelViewSet, basename='publication')


urlpatterns = []

urlpatterns += router.urls