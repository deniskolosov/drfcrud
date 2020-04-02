from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import AppModel
from .serializers import AppModelSerializer


class AppList(generics.ListCreateAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppModelSerializer


class AppDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppModelSerializer


class AppViewSet(viewsets.ViewSet):
    lookup_field = "api_key"

    def retrieve(self, request, api_key=None):
        queryset = AppModel.objects.all()
        app = get_object_or_404(queryset, api_key=api_key)
        serializer = AppModelSerializer(app)
        return Response(serializer.data)
