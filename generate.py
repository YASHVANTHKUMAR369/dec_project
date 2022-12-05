import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SNADHAN.settings')

import django
django.setup()

from snadhanapp.models import *
from faker import Faker
from random import *
faker = Faker()

def populate(n):
	for i in range(n):
		fcno = randint(1001,9999)
		fcname = faker.name()
		fcsubject = randint(8111111111,9999999999)
		fcmessage = faker.text()
		cuts_records = custome_details.objects.get_or_create(cno=fcno, cname=fcname, csubject=fcsubject, cmessage=fcmessage)

populate(20)