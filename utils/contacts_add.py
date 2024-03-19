import os
import sys
from datetime import datetime
from pathlib import Path

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from home.models import Home

    Home.objects.all().delete()

    fake = faker.Faker('pt_BR')

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        username= profile['name']
        password = fake.phone_number()
        created_date: datetime = fake.date_this_year()
       


        django_contacts.append(
            Home(
                username=username,
                password=password,
                email=email,
                created_date=created_date,
            )
        )

    if len(django_contacts) > 0:
        Home.objects.bulk_create(django_contacts)