"""Plan related tasks"""
from celery.utils.log import get_task_logger

from src.celery_app import celery

log = get_task_logger(__name__)


@celery.task()
def calculate_mb_available():
    """ADD CODE HERE"""
    pass
