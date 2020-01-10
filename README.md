## Requirements
* Python 3.5+
* Postgres 10+

## Starting the server
Everything is set up, including the database and some seed data. All you need to do is create the virtual environment with the dependencies and then migrate the database by running `FLASK_APP=att.py flask db upgrade`.

## Context
- Subscriptions run on billing cycles. For each billing cycle, a subscription will start on one plan, but can be upgraded or downgraded during the billing cycle. For example, a subscription might start on a 1GB plan and then upgrade to a 3GB plan mid-cycle after they've reached their available data limit. When they upgrade to the 3GB plan, they have an additional 2GB of data available to use before the end of the billing cycle.
- We have an `ATTPlanVersion` table to keep track of the plan a subscription is on at any given time. There is a `start_effective_date` and `end_effective_date` in this table. For the example above of a subscription starting on 1GB plan and upgrading to a 3GB plan mid-cycle, the rows in the table would look something like this:
```
# 1GB plan_id = 1
# 3GB plan_id = 2
{
    'id': 1,
    'subscription_id': '1',
    'plan_id': '1',
    'start_effective_date': '2019-11-01T00:00:00+00:00',
    'end_effective_date': '2019-12-01T00:00:00+00:00'
},
{
    'id': 2,
    'subscription_id': '1',
    'plan_id': '2',
    'start_effective_date': '2019-11-01T00:00:00+00:00',
    'end_effective_date': '2019-12-01T00:00:00+00:00'
}
```
- You might be wondering why we even bother with effective dates instead of just referencing the billing cycle. The problem comes when subscriptions are activated or expired mid-cycle. For subscriptions activated mid-cycle, the plan is effective starting when the subscription was activated. So the `start_effective_date` would be the subscription `activation_date`. Similarly, for expired subscriptions, the plan is only effective up as long as the subscription was `active` or `suspended`. So the `end_effective_date` would be the subscription `expiry_date`.
- The metric we are concerned about for this challenge is the available data. We need to calculate how much data we have available for each subscription for a billing cycle. For plans with effective dates that start or end mid-cycle, the data will be prorated based on how many days it was active during the cycle. For example, if a subscription is activated on a 3GB plan exactly midway through the cycle (ie. November 15th), then the available data for the November billing cycle will be 1.5GB.

## Challenge
1. Add code for the `calculate_mb_available` task in the `plans.py` tasks file. This should do the following:
- Query the subscriptions plans version table for any subscriptions `active` or `suspended` at any point during the given billing cycle.
- Calculate the `mb_available` for each subscription plan for the November billing cycle using the predefined data in the migration and save the results. You MUST use postgres functions for this, but utilize the SQLAlchemy ORM where possible in using these functions.
    - If a plan was upgraded or changed for a subscription during the billing cycle, the `mb_available` should be 0 for the old plan.
    - Make this function reusable for other billing cycles / months.
- Determine which plan the subscription was effective for which dates (starting effective date and ending effective date). Return those results as a list of tuples with the `subscription_id` and `plan_id`
    - For the example above with the 1GB plan and 3GB plan for a subscription, it should only return the 3GB plan with a starting effective date of the beginning of the cycle and ending effective date of the end of the cycle.
- Write tests to sufficiently cover the code you add.
2. Add an endpoint for `/api/subscriptions/{id}/att_plan_version/`. This should do the following:
- Accept a `billing_cycle_id` as a request parameter. If not provided, use the current billing cycle.
- Return the att plan that was effective for a given billing cycle with the effective date fields and the `mb_available`.