from django.shortcuts import render
from .forms import ContactForm



# Create your views here.

def index(request):
    
    return render(request, 'index.html')
  


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'request_confirm.html')
    form = ContactForm()
    dict_form1={
        'form': form
    }
   
    return render(request, 'contact.html',dict_form1)

     

