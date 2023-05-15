from django.contrib.auth.models import User, Group
from .models import Recipe
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecipeSerializer


class RicepeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    