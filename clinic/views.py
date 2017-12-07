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

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class DashView(TemplateView):
    template_name = 'dash.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class HelpView(TemplateView):
    template_name = 'about.html'

def PatientListView(request):
    patients_per_page = 15
    queryset_list = Patient.objects.all()
    page = request.GET.get('page', 1)

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(patient_id__icontains=query) |
            Q(national_id__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, patients_per_page)
    try:
        patient_list = paginator.page(page)
    except PageNotAnInteger:
        patient_list = paginator.page(1)
    except EmptyPage:
        patient_list = paginator.page(paginator.num_pages)

    total_number_of_pages = int(len(queryset_list)/patients_per_page)
    context = {
        "patient_list": patient_list,
        "total_page_count": total_number_of_pages,
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

def DoctorListView(request):
    doctors_per_page = 15
    queryset_list = Doctor.objects.all()
    page = request.GET.get('page', 1)

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(specialty__icontains=query) |
            Q(doctor_id__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, doctors_per_page)
    try:
        doctor_list = paginator.page(page)
    except PageNotAnInteger:
        doctor_list = paginator.page(1)
    except EmptyPage:
        doctor_list = paginator.page(paginator.num_pages)

    total_number_of_pages = int(len(queryset_list)/doctors_per_page)
    context = {
        "doctor_list": doctor_list,
        "total_page_count": total_number_of_pages,
    }

    return render(request, "doctor_list.html", context)

class DoctorDetailView(DetailView):
    model = Doctor

    def get_context_data(self, **kwargs):
        context = super(DoctorDetailView, self).get_context_data(**kwargs)
        context['doctor_visits'] = Visit.objects.filter(doctor = context['doctor'])
        return context

class DoctorUpdateView(UpdateView):
    redirect_field_name = 'clinic/doctor_detail.html'
    form_class = DoctorForm
    model = Doctor

class DoctorCreateView(CreateView):
    redirect_field_name = 'clinic/doctor_detail.html'
    form_class = DoctorForm
    model = Doctor

class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctor_list')


#ERROR Handling
def handler404(request):
    response = render_to_response('clinic/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('clinic/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
