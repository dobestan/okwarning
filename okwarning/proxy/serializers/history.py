from rest_framework import serializers

from proxy.models import History


class HistoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = (
            'url',
        )
