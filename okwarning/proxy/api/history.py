from rest_framework.generics import ListCreateAPIView
from rest_framework import filters

from proxy.models import History
from proxy.serializers import HistoryModelSerializer


class HistoryListCreateAPIView(ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistoryModelSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('url', )
