from django import forms

from .models import Doctor, Patient, Visit
from .choices import SEX, BLOOD_TYPE

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        sex = forms.ChoiceField(choices=SEX)
        blood_type = forms.ChoiceField(choices=BLOOD_TYPE)

        fields = ('patient_id', 'national_id', 'first_name',
                'last_name', 'address', 'sex', 'birthdate',
                'blood_type', 'language', 'phone_num',
                'photo_ID',)

        widgets = {
            'patient_id': forms.TextInput(),
            'national_id': forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'address': forms.TextInput(),
            'birthdate': forms.DateInput(),
            'language': forms.TextInput(),
            'phone_num': forms.TextInput(),
            'photo_ID': forms.FileInput(),
        }

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ('doctor_id', 'first_name',
                'last_name', 'specialty',)

        widgets = {
            'doctor_id': forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'specialty': forms.TextInput(),
        }

class VisitForm(forms.ModelForm):

    class Meta:
        model = Visit
        fields = ('patient', 'doctor', 'symptoms', 'notes', 'recommendation')
