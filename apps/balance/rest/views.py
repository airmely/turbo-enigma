from django.contrib.auth import get_user_model
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.balance.models import Balance, Transaction
from apps.balance.rest.serializers import (
    BalanceDetailSerializer,
    BalanceSerializer,
    SendAmountUserToUserSerializer,
    TopUpBalanceSerializer,
    TransactionHistorySerializer,
)

User = get_user_model()


class GetBalanceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: BalanceSerializer(),
        },
        operation_summary="Get Balance",
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
                action=Transaction.DEPOSIT,
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

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TransactionHistorySerializer(),
        },
        operation_summary="User transaction history",
    )
    def get(self, request: Request) -> Response:
        history = Transaction.objects.filter(
            Q(receiver=request.user) | Q(sender=request.user),
        )
        serializer = TransactionHistorySerializer(history, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class SendAmountUserToUserAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=SendAmountUserToUserSerializer,
    )
    def post(self, request: Request, *args, **kwargs) -> Response:  # noqa
        serializer = SendAmountUserToUserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            receiver_id = kwargs["receiver_id"]
            try:

                receiver = User.objects.get(id=receiver_id)
            except User.DoesNotExist:
                return Response(
                    {"detail": "User does not exist."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            if receiver == request.user:
                return Response(
                    {"detail": "You cannot send money to yourself."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            amount = serializer.validated_data["amount"]
            sender = request.user

            sender_balance = Balance.objects.get(owner=sender)
            receiver_balance = receiver.balance

            if sender_balance.amount < amount:
                return Response(
                    {"detail": "There are insufficient funds in the account."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            sender_balance.amount -= amount
            receiver_balance.amount += amount

            sender_balance.save()
            receiver_balance.save()

            Transaction.objects.create(
                sender=sender,
                receiver=receiver,
                amount=amount,
                action=Transaction.WITHDRAW,
            )

            return Response(
                {"detail": "The translation was completed successfully."},
                status=status.HTTP_200_OK,
            )
