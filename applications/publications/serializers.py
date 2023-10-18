from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Year
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class PublicationNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicationName
        fields = '__all__'