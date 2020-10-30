from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import AutofillUrlForm

from .autofiller import autofiller

def user_input(request):
    # Create a form instance and populate it with data from the request (binding):
    form = AutofillUrlForm(request.POST)

    # Check if the form is valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        user_autofill_url = form.cleaned_data["autofill_url"]
        user_clinical_teacher = form.cleaned_data["clinical_teacher"]

        result = autofiller(user_autofill_url)
        return HttpResponse(result)
        # redirect to a new URL:
        """return HttpResponseRedirect(reverse('all-borrowed') )"""
        """return HttpResponse(user_autofill_url)"""
        #result = autofiller(user_autofill_url)
        #return HttpResponse(user_autofill_url + user_clinical_teacher)

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_user_autofill_url = "https://redcap.mc.ntu.edu.tw/surveys/?s="
        proposed_user_clinical_teacher = "1"
        form = AutofillUrlForm(initial={'autofill_url': proposed_user_autofill_url, 'clinical_teacher' : proposed_user_clinical_teacher})

    context = {
        'form': form,
    }

    return render(request, 'formautofiller/user_input.html', context)