from django.db import models

# Create your models here.



class Contact(models.Model):

    c_name = models.CharField(max_length=255)
    c_subject = models.CharField(max_length=150)
    c_email = models.EmailField()
    c_message = models.TextField()     