from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import AutofillUrlForm
from .tasks import long_running_operation

import logging
#logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

#from .autofiller import autofiller

def user_input(request):
    # Create a form instance and populate it with data from the request (binding):
    form = AutofillUrlForm(request.POST)
    # set task_id to 0 to hide process template
    task_id = 0

    # Check if the form is valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        user_autofill_url = form.cleaned_data["autofill_url"]
        user_clinical_teacher = form.cleaned_data["clinical_teacher"]
        
        # Create Task
        autofill_task = long_running_operation.delay(user_autofill_url, user_clinical_teacher)
        print("create task complete!@views.py")
        logger.info("create task complete!@views.py")
        # Get ID
        task_id = autofill_task.task_id
        print("get task id complete!@views.py")
        logger.info("get task id complete!@views.py")

        #result = autofiller(user_autofill_url, user_clinical_teacher)
        #return HttpResponse("Processing...")
        # redirect to a new URL:
        """return HttpResponseRedirect(reverse('all-borrowed') )"""
        """return HttpResponse(user_autofill_url)"""
        #result = autofiller(user_autofill_url)
        #return HttpResponse(user_autofill_url + user_clinical_teacher)

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_user_autofill_url = ""
        proposed_user_clinical_teacher = "1"
        form = AutofillUrlForm(initial={'autofill_url': proposed_user_autofill_url, 'clinical_teacher' : proposed_user_clinical_teacher})

    context = {
        'form': form,
        'task_id': task_id,
    }

    return render(request, 'formautofiller/progress.html', context)