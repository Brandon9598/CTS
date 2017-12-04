from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from clinic.models import Patient, Doctor, Visit
from django.utils import timezone
from clinic.forms import PatientForm, DoctorForm, VisitForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class DashView(TemplateView):
    template_name = 'dash.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class HelpView(TemplateView):
    template_name = 'about.html'

def PatientListView(request):
    queryset_list = Patient.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(patient_id__icontains=query) |
            Q(national_id__icontains=query)
        ).distinct()

    context = {
        "patient_list": queryset_list,
    }

    return render(request, "patient_list.html", context)

#class PatientListView(ListView):
#    model = Patient
#
#    def get_queryset(self):
#        return Patient.objects.all()

class PatientDetailView(DetailView):
    model = Patient

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        context['patient_visits'] = Visit.objects.filter(patient = context['patient'])
        context_list = ""
        for item in context:
            context_list += item + " "
        context["test"] = context_list
        return context

class PatientCreateView(CreateView):
    redirect_field_name = 'clinic/patient_detail.html'

    form_class = PatientForm

    model = Patient

class PatientUpdateView(UpdateView):
    redirect_field_name = 'clinic/patient_detail.html'

    form_class = PatientForm

    model = Patient

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list')

class VisitListView(ListView):
    model = Visit

    def get_queryset(self):
        return Visit.objects.all()

class VisitDetailView(DetailView):
    model = Visit

class VisitUpdateView(UpdateView):
    redirect_field_name = 'clinic/visit_detail.html'
    form_class = VisitForm
    model = Visit

class VisitCreateView(CreateView):
    redirect_field_name = 'clinic/visit_detail.html'
    form_class = VisitForm
    model = Visit

class VisitDeleteView(DeleteView):
    model = Visit
    success_url = reverse_lazy('visit_list')


#Add the doctor and visit views
#Add functions that require a pk match
