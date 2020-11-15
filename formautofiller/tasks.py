from __future__ import absolute_import, unicode_literals
from celery import shared_task


from .autofiller import autofiller

from celery_progress.backend import ProgressRecorder
import time

@shared_task(bind=True)
def long_running_operation(self, user_autofill_url, user_clinical_teacher):
    print("long running operation started!@tasks.py")

    autofiller(self,user_autofill_url, user_clinical_teacher)