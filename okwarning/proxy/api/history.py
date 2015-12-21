from rest_framework.generics import ListCreateAPIView
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status

from proxy.models import History
from proxy.serializers import HistoryModelSerializer


class HistoryListCreateAPIView(ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistoryModelSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            History.objects.get_domains(filter=request.GET.get('search', None)),
            status=status.HTTP_200_OK,
        )
