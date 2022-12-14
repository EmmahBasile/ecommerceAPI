from dataclasses import fields
from importlib.metadata import files
from rest_framework import serializers
from .models import Category, Book, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageURL',
            'status',
            'date_created'
        )
        model = Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'description',
            'imageURL',
            'status',
            'date_created'
        )
        model = Product
