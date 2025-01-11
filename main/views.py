# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST.get('phone', '')
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, phone=phone, message=message)
        return redirect('home')
    return render(request, 'main/home.html')

from django.http import HttpResponse

def home(request):
    return render(request, 'main/index.html')

# def home(request):
#     return render(request,'main/base.html')

from .models import Education, Project  # Assuming these models exist.

# def home(request):
#     education_list = Education.objects.all()
#     project_list = Project.objects.all()
#     return render(request, 'main/base.html', {'education_list': education_list, 'project_list': project_list})


from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

def home(request):
    return render(request, 'main/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Compose email
        subject = f"Portfolio Contact: {name}"
        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        # Send email
        try:
            send_mail(
                subject,
                body,
                'your-email@example.com',  # Replace with your sender email (e.g., Gmail)
                ['dsanket373@gmail.com'],  # Replace with your email
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'An error occurred while sending the message. Please try again.')

        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Allows POST requests without a CSRF token for testing purposes (use cautiously in production)
def contact_form_submission(request):
    if request.method == 'POST':
        try:
            # Parse JSON data sent by the frontend
            data = json.loads(request.body)

            name = data.get('name', 'No Name Provided')
            mobile_number = data.get('mobile_number', 'No Mobile Number Provided')
            email = data.get('email', 'No Email Provided')
            message =data.get('message')

            # Compose email content
            subject = 'New Contact Form Submission'
            message = f"""
            You have received a new contact form submission:
            Name: {name}
            Mobile Number: {mobile_number}
            Email: {email}
            Message: {message}
            """
            recipient = 'dsanket373@gmail.com'

            # Send email
            send_mail(
                subject,
                message,
                'dsanket373@gmail.com',  # Sender's email
                [recipient],  # Recipient's email
                fail_silently=False,
            )
            
            return JsonResponse({'success': True, 'message': 'Email sent successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
