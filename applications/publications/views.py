from rest_framework import viewsets
from .models import *
from .serializers import *


class CountryModelViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class YearModelViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class GenreModelViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublicationNameModelViewSet(viewsets.ModelViewSet):
    queryset = PublicationName.objects.all()
    serializer_class = PublicationNameSerializer