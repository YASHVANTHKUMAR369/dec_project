from django.db import models

class customer_details(models.Model):
    mobile_no = models.IntegerField()
    name = models.CharField(max_length= 20)
    mail = models.CharField(max_length= 30)
    subject = models.CharField(max_length= 30)
    message = models.CharField(max_length= 100)
# Create your models here.
