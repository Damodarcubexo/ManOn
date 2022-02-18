from celery import Celery
# from .views import SentMailView
from celery.utils.log import get_task_logger
from celery import shared_task

from time import sleep

logger = get_task_logger(__name__)


@shared_task(name='my_first_task')
def my_first_task(duration):
    sleep(duration)
    return ("task_done")

@shared_task(name="email_sent")
def email_sent(duration):
    subject = 'Reset Your Password'
