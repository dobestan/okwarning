from rest_framework.generics import ListCreateAPIView

from proxy.models import History
from proxy.serializers import HistoryModelSerializer


class HistoryListCreateAPIView(ListCreateAPIView):
    serializer_class = HistoryModelSerializer

    def get_queryset(self):
        return History.objects.order_by().distinct('url', )
