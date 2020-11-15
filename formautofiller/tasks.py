from __future__ import absolute_import
from celery import shared_task


from .autofiller import autofiller


@shared_task
def long_running_operation(user_autofill_url, user_clinical_teacher):
    print("long running operation started!@tasks.py")
    autofiller(self,user_autofill_url, user_clinical_teacher)
    return