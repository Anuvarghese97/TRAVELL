from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


        labels = {
           'c_name':'Name:',
           'c_subject':'subject:',
           'c_email':'Email:',
           'c_message':'Message:',
        
        }        