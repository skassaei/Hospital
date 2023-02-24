from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Triage
from .form import TriageForm
from django.shortcuts import render
from django.db.models import CharField, Value as V
from .models import Triage
from django.db.models.functions import Concat
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
# Create your views here.

#checks if user is a station
def station_check(user):
    return user.groups.filter(name__in=['stations']).exists()


#checks if user is not a station
@login_required()
def home_view(request):
    name = request.user.get_full_name()
    return render(request, "home.html", {'name':name})



def add_triage(request):
    #if station_check(request.user):

        submitted = False  #if this is the first time visiting the form
        if request.method == "POST": # if they hit submit in the form
            form = TriageForm(request.POST) # pass what ever they have requested(submited) to the database?
            if form.is_valid(): #check if all the fields in the form are valid 
                form.save() # save the form to model
                return HttpResponseRedirect('/add_triage?submitted=True') # we want to return the user back to the page sth when it successfully saved. need to import HttpResponseRedirect from django
        else: #they haven't fill out the form yet 

            # create object of form
            form = TriageForm
            if 'submitted' in request.GET: # when HttpResponse redirect back to the page it will send the submitted=True to GET so 
                submitted = True #if they have submitted we can change this to true
        return render(request,'add_triage_form.html',{'form': form, 'submitted':submitted}) #passing our form and submitted which is false if nothing has happend yet
    #else:
    #    raise PermissionDenied

def patients_list(request):
    patients_list = Triage.objects.all()
    return render(request, "display_all_patients.html",{'patients_list':patients_list})

def show_triage(request,patient_id):
    triage=Triage.objects.get(pk=patient_id)
    #passing the patient form to the page:
    return render(request,'show_triage_details.html',{'triage':triage})

def error_404(request, exception):
    return render(request, '404.html')