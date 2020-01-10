"""Plans and Service related models and database functionality"""
from src.models.base import db


class ATTPlanVersion(db.Model):
    """Model class to represent ATT plan version

    Custom versioning class to keep track of plans enabled ATT side
    """
    __tablename__ = "att_plan_versions"
    id = db.Column(db.Integer, primary_key=True)
    subscription_id = db.Column(
        db.Integer, db.ForeignKey("subscriptions.id"), nullable=False
    )
    subscription = db.relationship(
        "Subscription", back_populates="att_plan_versions", lazy="select"
    )
    plan_id = db.Column(
        db.String(30), db.ForeignKey("plans.id"), nullable=False
    )
    plan = db.relationship("Plan", foreign_keys=[plan_id], lazy="select")

    start_effective_date = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    end_effective_date = db.Column(db.TIMESTAMP(timezone=True), nullable=False)

    mb_available = db.Column(db.BigInteger)

    def __repr__(self):  # pragma: no cover
        return (
            f"<{self.__class__.__name__}: {self.subscription_id}, "
            f"{str(self.plan_id)} ({self.start_effective_date} - "
            f"{self.end_effective_date}) "
        )


class Plan(db.Model):
    """Model class to represent mobile service plans"""
    __tablename__ = "plans"
    id = db.Column(db.String(30), primary_key=True)
    description = db.Column(db.String(200))
    # amount of data available for a given billing cycle
    mb_available = db.Column(db.BigInteger)
    is_unlimited = db.Column(db.Boolean)

    def __repr__(self):  # pragma: no cover
        return (
            f"<{self.__class__.__name__}: {self.id} ({self.description})>"
        )
