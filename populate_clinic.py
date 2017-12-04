import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTS.settings')

import django
django.setup()

## Fake pupulation script
import random
from clinic.models import Patient, Visit, Doctor
from faker import Faker

fakegen = Faker()

def clean(unclean):
    unclean = unclean.replace('(', '')
    unclean = unclean.replace(')', '')
    unclean = unclean.replace('-', '')
    unclean = unclean.replace('.', '')
    unclean = unclean.replace('x', '')
    unclean = unclean.replace('+', '')
    return unclean

def populate(N=5):
    count = 0
    for entry in range(N):
        fake_patient_id = fakegen.phone_number()
        fake_patient_id = clean(fake_patient_id)
        fake_national_id = fakegen.phone_number()
        fake_national_id = clean(fake_national_id)
        fake_fname = fakegen.first_name()
        fake_lname  = fakegen.last_name()
        fake_address = fakegen.address()

        patient = Patient.objects.get_or_create(first_name = fake_fname,
            last_name = fake_lname, patient_id=fake_patient_id,
            national_id = fake_national_id)[0]
        print(count)
        count += 1

if __name__ == '__main__':
    print("Populating")
    populate(50000)
    print("Finished Populating")
