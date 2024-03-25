from django.shortcuts import render
from .models import RegisterGDSC
from django.contrib import messages

# Create your views here.


def HomePage(request):

    registration = RegisterGDSC.objects.all()

    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']

        # Check if a user with the same name and email already exists
        if RegisterGDSC.objects.filter(name=fullname, email=email).exists():
            messages.error(
                request, "Looks like we have seen this email before. You are already Registered😊")
        else:
            education = request.POST['education']
            school = request.POST['school']
            whatsapp_number = request.POST['whatsapp_number']

            registration_form = RegisterGDSC(name=fullname, education=education,
                                             school=school, whatsapp_number=whatsapp_number, email=email)

            registration_form.save()

            messages.success(
                request, "Wohooo, You registered for CDS 24' successfully, Can't wait to see you there😊")

    context = {
        'registration': registration
    }
    return render(request, 'index.html', context)


def ContactUs(request):

    return render(request, 'contact.html')
