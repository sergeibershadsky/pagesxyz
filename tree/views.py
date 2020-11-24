from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Page
from .serializers import PageSerializer


class PagesViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated, ]
