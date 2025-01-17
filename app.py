"""Application to test idempotency with AWS Lambda using DynamoDB."""

from dataclasses import dataclass, field
from uuid import uuid4

from aws_lambda_powertools.utilities.idempotency import (
    DynamoDBPersistenceLayer,
    idempotent,
)
from aws_lambda_powertools.utilities.typing import LambdaContext

persistence_layer = DynamoDBPersistenceLayer(table_name="IdempotencyTable")


@dataclass
class Payment:
    user_id: str
    product_id: str
    payment_id: str = field(default_factory=lambda: f"{uuid4()}")


class PaymentError(Exception): ...


@idempotent(persistence_store=persistence_layer)
def lambda_handler(event: dict, context: LambdaContext):
    try:
        payment: Payment = create_subscription_payment(event)
        return {
            "payment_id": payment.payment_id,
            "message": "success",
            "statusCode": 200,
        }
    except Exception as exc:
        raise PaymentError(f"Error creating payment {str(exc)}")


def create_subscription_payment(event: dict) -> Payment:
    return Payment(**event)
