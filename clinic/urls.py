from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.DashView.as_view(),name='dash'),
    url(r'^patient/$',views.PatientListView ,name='patient_list'),
    url(r'^patient/(?P<pk>\d+)$',views.PatientDetailView.as_view(),name='patient_detail'),
    url(r'^patient/add$',views.PatientCreateView.as_view(),name="patient_create"),
    url(r'^patient/edit/(?P<pk>\d+)$',views.PatientUpdateView.as_view(),name='patient_update'),
    url(r'^patient/remove/(?P<pk>\d+)$', views.PatientDeleteView.as_view(),name="patient_delete"),
    url(r'^visits/$',views.VisitListView.as_view(),name="visit_list"),
    url(r'^visits/(?P<pk>\d+)$',views.VisitDetailView.as_view(),name='visit_detail'),
    url(r'^visits/add$',views.VisitCreateView.as_view(),name="visit_create"),
    url(r'^visits/edit/(?P<pk>\d+)$',views.VisitUpdateView.as_view(),name='visit_update'),
    url(r'^visits/remove/(?P<pk>\d+)$', views.VisitDeleteView.as_view(),name="visit_delete"),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^help/$',views.HelpView.as_view(),name="help")
]
