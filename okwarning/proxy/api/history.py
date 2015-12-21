from rest_framework.generics import CreateAPIView

from proxy.serializers import HistoryModelSerializer


class HistoryCreateAPIView(CreateAPIView):
    serializer_class = HistoryModelSerializer
