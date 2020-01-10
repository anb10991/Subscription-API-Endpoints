"""Service code schemas to assist with plan serialization"""
from marshmallow import fields, Schema


class ATTPlanVersionSchema(Schema):
    """Schema class to handle serialization of att plan version data"""
    id = fields.Integer()
    subscription_id = fields.Integer()
    plan_id = fields.String()
    start_effective_date = fields.DateTime()
    end_effective_date = fields.DateTime()
    mb_available = fields.Integer()


class PlanSchema(Schema):
    """Schema class to handle serialization of plan data"""
    id = fields.String()
    description = fields.String()
    mb_available = fields.Integer()
    is_unlimited = fields.Boolean()
