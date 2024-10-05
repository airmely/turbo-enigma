from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from apps.balance.models import Transaction, Balance
from apps.balance.rest.serializers import (
    TopUpBalanceSerializer,
    BalanceDetailSerializer,
    BalanceSerializer,
    TransactionHistorySerializer,
)

User = get_user_model()


class GetBalanceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=BalanceSerializer,
    )
    def get(self, request: Request) -> Response:
        try:
            balance = Balance.objects.get(owner=request.user)
            serializer = BalanceSerializer(balance)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        except Balance.DoesNotExist:
            return Response(
                {"detail": "No balance found."},
                status=status.HTTP_404_NOT_FOUND,
            )


class TopUpBalanceAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=TopUpBalanceSerializer,
        responses={
            status.HTTP_200_OK: BalanceDetailSerializer(),
        },
        operation_summary="Top Up Balance",
    )
    def post(self, request: Request) -> Response:
        serializer = TopUpBalanceSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = request.user
            user.balance.amount += serializer.validated_data["amount"]
            user.balance.save()
            bank = User.objects.get(username="Main bank")
            Transaction.objects.create(
                sender=bank,
                receiver=user,
                amount=serializer.validated_data["amount"],
            )
            return Response(
                {
                    "balance": user.balance.amount,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class TransactionHistoryAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        history = Transaction.objects.filter(receiver=request.user)
        serializer = TransactionHistorySerializer(history, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
