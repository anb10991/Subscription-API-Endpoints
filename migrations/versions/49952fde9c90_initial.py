"""initial migration

Revision ID: 49952fde9c90
Revises:
Create Date: 2019-09-28 13:11:26.043849

"""
from datetime import datetime, timezone

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '49952fde9c90'
down_revision = None
branch_labels = None
depends_on = None


def populate_billing_cycles(billing_cycles):
    op.bulk_insert(billing_cycles, [
        {
            'id': 1,
            'start_date': datetime(2019, 8, 1, tzinfo=timezone.utc),
            'end_date': datetime(2019, 9, 1, tzinfo=timezone.utc),
        },
        {
            'id': 2,
            'start_date': datetime(2019, 9, 1, tzinfo=timezone.utc),
            'end_date': datetime(2019, 10, 1, tzinfo=timezone.utc),
        },
        {
            'id': 3,
            'start_date': datetime(2019, 10, 1, tzinfo=timezone.utc),
            'end_date': datetime(2019, 11, 1, tzinfo=timezone.utc),
        }
    ])


def populate_plans(plans):
    op.bulk_insert(plans, [
        {
            'id': 1,
            'description': '1GB Monthly Data Plan',
            'mb_available': '1024',
            'is_unlimited': False
        },
        {
            'id': 2,
            'description': '5GB Monthly Data Plan',
            'mb_available': '5120',
            'is_unlimited': False
        },
        {
            'id': 3,
            'description': 'Unlimited Monthly Data Plan',
            'mb_available': '10240',
            'is_unlimited': True
        }
    ])


def populate_att_plan_versions(att_plan_versions):
    op.bulk_insert(att_plan_versions, [
        {
            'id': 1,
            'subscription_id': '1',
            'plan_id': '2',
            'start_effective_date': datetime(2019, 11, 1, tzinfo=timezone.utc),
            'end_effective_date': datetime(2019, 12, 1, tzinfo=timezone.utc)
        },
        {
            'id': 2,
            'subscription_id': '1',
            'plan_id': '3',
            'start_effective_date': datetime(2019, 11, 1, tzinfo=timezone.utc),
            'end_effective_date': datetime(2019, 12, 1, tzinfo=timezone.utc)
        },
        {
            'id': 3,
            'subscription_id': '1',
            'plan_id': '1',
            'start_effective_date': datetime(2019, 11, 1, tzinfo=timezone.utc),
            'end_effective_date': datetime(2019, 12, 1, tzinfo=timezone.utc)
        },
        {
            'id': 4,
            'subscription_id': '2',
            'plan_id': '1',
            'start_effective_date': datetime(2019, 11, 3, tzinfo=timezone.utc),
            'end_effective_date': datetime(2019, 12, 1, tzinfo=timezone.utc)
        },
        {
            'id': 5,
            'subscription_id': '4',
            'plan_id': '1',
            'start_effective_date': datetime(2019, 11, 10, tzinfo=timezone.utc),
            'end_effective_date': datetime(2019, 11, 28, tzinfo=timezone.utc)
        },
        {
            'id': 6,
            'subscription_id': '4',
            'plan_id': '2',
            'start_effective_date': datetime(2019, 11, 10, tzinfo=timezone.utc),
            'end_effective_date': datetime(2019, 11, 28, tzinfo=timezone.utc)
        },
        {
            'id': 7,
            'subscription_id': '5',
            'plan_id': '1',
            'start_effective_date': datetime(2019, 11, 1, tzinfo=timezone.utc),
            'end_effective_date': datetime(2019, 11, 3, tzinfo=timezone.utc)
        },
        {
            'id': 8,
            'subscription_id': '5',
            'plan_id': '3',
            'start_effective_date': datetime(2019, 11, 1, tzinfo=timezone.utc),
            'end_effective_date': datetime(2019, 11, 3, tzinfo=timezone.utc)
        },
        {
            'id': 9,
            'subscription_id': '6',
            'plan_id': '1',
            'start_effective_date': datetime(2019, 11, 30, tzinfo=timezone.utc),
            'end_effective_date': datetime(2019, 12, 1, tzinfo=timezone.utc)
        }
    ])


def populate_subscriptions(subscriptions):
    op.bulk_insert(subscriptions, [
        {
            'id': 1,
            'phone_number': '1111111111',
            'status': 'active',
            'plan_id': 3,
            'activation_date': datetime(2019, 9, 12, tzinfo=timezone.utc),
            'expiry_date': None
        },
        {
            'id': 2,
            'phone_number': '2222222222',
            'status': 'suspended',
            'plan_id': 1,
            'activation_date': datetime(2019, 11, 3, tzinfo=timezone.utc),
            'expiry_date': None
        },
        {
            'id': 3,
            'phone_number': '3333333333',
            'status': 'new',
            'plan_id': 2,
            'activation_date': None,
            'expiry_date': None
        },
        {
            'id': 4,
            'phone_number': '4444444444',
            'status': 'expired',
            'plan_id': 2,
            'activation_date': datetime(2019, 11, 10, tzinfo=timezone.utc),
            'expiry_date': datetime(2019, 11, 28, tzinfo=timezone.utc)
        },
        {
            'id': 5,
            'phone_number': '5555555555',
            'status': 'expired',
            'plan_id': 3,
            'activation_date': datetime(2019, 10, 10, tzinfo=timezone.utc),
            'expiry_date': datetime(2019, 11, 3, tzinfo=timezone.utc)
        },
        {
            'id': 6,
            'phone_number': '7777777777',
            'status': 'suspended',
            'plan_id': 1,
            'activation_date': datetime(2019, 11, 30, tzinfo=timezone.utc),
            'expiry_date': None
        },
        {
            'id': 7,
            'phone_number': '8888888888',
            'status': 'new',
            'plan_id': 2,
            'activation_date': None,
            'expiry_date': None
        }
    ])


def upgrade():
    billing_cycles = op.create_table('billing_cycles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('start_date', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('end_date', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    populate_billing_cycles(billing_cycles)

    plans = op.create_table('plans',
        sa.Column('id', sa.String(length=30), nullable=False),
        sa.Column('description', sa.String(length=200), nullable=True),
        sa.Column('mb_available', sa.BigInteger(), nullable=True),
        sa.Column('is_unlimited', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    populate_plans(plans)

    subscriptions = op.create_table('subscriptions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('phone_number', sa.String(length=10), nullable=True),
        sa.Column('status', postgresql.ENUM('new', 'active', 'suspended', 'expired', name='subscriptionstatus'), nullable=True),
        sa.Column('plan_id', sa.String(length=30), nullable=False),
        sa.ForeignKeyConstraint(['plan_id'], ['plans.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    populate_subscriptions(subscriptions)

    att_plan_versions = op.create_table('att_plan_versions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('subscription_id', sa.Integer(), nullable=False),
        sa.Column('plan_id', sa.String(length=30), nullable=False),
        sa.Column('start_effective_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('end_effective_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('mb_available', sa.BigInteger(), nullable=True),
        sa.ForeignKeyConstraint(['plan_id'], ['plans.id'], name=op.f('fk_att_plans_version_plan_id')),
        sa.ForeignKeyConstraint(['subscription_id'], ['subscriptions.id'], name=op.f('fk_att_plans_version_subscription_id')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_att_plans_version'))
    )
    populate_att_plan_versions(att_plan_versions)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('att_plan_versions')
    op.drop_table('subscriptions')
    op.drop_table('plans')
    op.drop_table('billing_cycles')
    # ### end Alembic commands ###
