"""Subscription schemas to assist with sub serialization"""
from marshmallow import fields, Schema, validate

from src.schemas.plans import PlanSchema


class SubscriptionSchema(Schema):
    """Schema class to handle serialization of subscription data"""
    id = fields.Integer()
    phone_number = fields.String()

    status = fields.String()
    status_effective_date = fields.DateTime()

    plan_id = fields.String()
    plan = fields.Nested(PlanSchema, dump_only=True)
