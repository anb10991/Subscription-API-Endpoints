"""Subscription related models and database functionality"""
from datetime import datetime
from enum import Enum

from sqlalchemy.dialects.postgresql import ENUM

from src.models.base import db


class SubscriptionStatus(Enum):
    """Enum representing possible subscription statuses"""
    new = "new"
    active = "active"
    suspended = "suspended"
    expired = "expired"


class Subscription(db.Model):
    """Model class to represent ATT subscriptions"""

    __tablename__ = "subscriptions"

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(10))
    status = db.Column(ENUM(SubscriptionStatus), default=SubscriptionStatus.new)
    activation_date = db.Column(db.TIMESTAMP(timezone=True), nullable=True)
    expiry_date = db.Column(db.TIMESTAMP(timezone=True), nullable=True)

    plan_id = db.Column(db.String(30), db.ForeignKey("plans.id"), nullable=False)
    plan = db.relationship("Plan", foreign_keys=[plan_id], lazy="select")

    def __repr__(self):  # pragma: no cover
        return (
            f"<{self.__class__.__name__}: {self.id} ({self.status}), "
            f"phone_number: {self.phone_number or '[no phone number]'}, ",
            f"plan: {self.plan_id}>"
        )

    @classmethod
    def get_subscriptions(cls, **kwargs):
        """Gets a list of Subscription objects using given kwargs

        Generates query filters from kwargs param using base class method

        Args:
            kwargs: key value pairs to apply as filters

        Returns:
            list: objects returned from query result

        """
        return cls.query.filter(**kwargs).all()
