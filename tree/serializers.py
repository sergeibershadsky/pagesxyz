from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Page


class PageSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, read_only=True)

    # def get_fields(self):
    #     fields = super(PageSerializer, self).get_fields()
    #     return fields

    class Meta:
        model = Page
        fields = ['id', 'name', 'text', 'children', 'parent']
        extra_kwargs = {
            'parent': {'write_only': True}
        }
