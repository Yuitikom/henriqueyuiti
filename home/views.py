from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail
from .forms import ContactForm
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('home/email/email.html', {
                'name':name,
                'email':email,
                'message':message,
            }
            )

            send_mail('From Site', 'Message', 'noreply@henriqueportifolio.com', [settings.EMAIL_HOST_USER], html_message=html )
            messages.success(request, 'Form submission successful')        
    project_obj = Project.objects.all()
    form = ContactForm()
    return render(request, 'home/index.html', {'project_obj':project_obj, 'form':form})
