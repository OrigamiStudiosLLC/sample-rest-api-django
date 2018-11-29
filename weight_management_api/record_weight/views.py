from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from weight_management_api.record_weight.serializers import UserWeightSerializer
from .models import UserWeight


class UserWeightView(APIView):
    """
    API to list user's weights.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Lists the user's weights.
        :param dict request: request object.
        :param list args: list of additional arguments.
        :param dict kwargs: dictionary if additional key word arguments.
        :return: HTTP response
        """
        user_weights = UserWeight.objects.filter(user=request.user)
        serialized_data = UserWeightSerializer(user_weights, many=True)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        """
        Saves the weight of user.
        :param dict request: request object.
        :param list args: list of additional arguments.
        :param dict kwargs: dictionary if additional key word arguments.
        :return: HTTP response
        """
        serializer = UserWeightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_weight = UserWeight(
            user=request.user,
            weight=serializer.validated_data.get('weight')
        )
        user_weight.save()
        return Response({'message': 'Weight entered successfully!'}, status=status.HTTP_201_CREATED)
