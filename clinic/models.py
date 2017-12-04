from django.db import models
from django.utils import timezone
from .choices import SEX, BLOOD_TYPE
from django.core.urlresolvers import reverse

# Create your models here.
class Patient(models.Model):
    patient_id = models.CharField(max_length=30, default="0000000000")
    national_id = models.CharField(max_length=30, default="0000000000")
    first_name = models.CharField(max_length=200, default="blank")
    last_name = models.CharField(max_length=200, default="blank")
    address = models.CharField(max_length=80, default="blank")
    created_date = models.DateTimeField(default=timezone.now)
    sex = models.CharField(choices=SEX, default='F', max_length=1)
    birthdate = models.DateTimeField(default=timezone.now)
    blood_type = models.IntegerField(choices=BLOOD_TYPE, default=0)
    language = models.CharField(max_length=20, default="blank")
    phone_num = models.IntegerField(default="18005000000")
    photo_ID = models.ImageField(upload_to = 'images/', blank=True)

    def get_absolute_url(self):
        return reverse("patient_detail",kwargs={"pk":self.pk})

    def __str__(self):
        return self.first_name + " " + self.last_name + ": " + self.patient_id

class Doctor(models.Model):
    doctor_id = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)
    #patients = models.ManyToManyField('clinic.Patient', default=None)

    def get_absolute_url(self):
        return reverse("doctor_detail",kwargs={"pk":self.pk})

    def __str__(self):
        return self.first_name + " " + self.last_name

class Visit(models.Model):
    patient = models.ForeignKey('clinic.Patient', related_name='visit')
    doctor = models.ForeignKey('clinic.Doctor', related_name='visit')
    symptoms = models.TextField(blank=True)
    visit_date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    recommendation = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("visit_list")

    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name + " saw Dr. " + self.doctor.last_name
