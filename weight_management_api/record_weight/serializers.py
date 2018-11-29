from rest_framework import serializers

from .models import UserWeight


class UserWeightSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserWeight model.
    """
    class Meta:
        model = UserWeight
        fields = ('weight', 'date_created')

    def to_representation(self, instance):
        return {
            'weight': instance.weight,
            'date_created': instance.date_created
        }
