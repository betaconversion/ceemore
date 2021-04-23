from django.shortcuts import render
from django.http import JsonResponse
from .models import Reservatioin
from django.core.mail import send_mail
from django.utils import timezone
# Create your views here.


com_email = ["samuelaniekan680@gmail.com"]

def home(request):
    return render(request,"index.html")


def service(request):
    return render(request,"services.html")


def about(request):
    return render(request,"about-us.html")


def gallery(request):
    return render(request,"gallery.html")

def contact_us(request):
    return render(request,"contact.html")


def check(date):
    qs = Reservatioin.objects.all()
    for book in qs:
        if book.time_to_meet >= date:
            return False
        else:
            return True
             



def reservation(request):
    date = request.POST["date"]
    phone = request.POST["phone"]
    email = request.POST["email"]
    now = timezone.now()
    re = check(date)
    if re == False:
        return JsonResponse({"context":"soory we are already booked"})
    else:
        body = f"Email address : {email} - Phone number : {phone} - Time: {date}"
        subject = "New book available"
        from_email =  email
        to = [email]
        send_mail(subject,body,from_email,com_email)
        Reservatioin.objects.create(time_to_meet=date,name=email,email=email,phone_number=phone)
        return JsonResponse({"context":"Thanks for we will soon get in touch with you"})
  


def message(request):
    
    phone = request.POST["phone"]
    from_email = request.POST["email"]
    message = request.POST["message"]
    fuul_name = request.POST["fuul_name"]
    now = timezone.now()
    subject = f"Message from {fuul_name} tel:{phone} on Ceemore.com "
    send_mail(subject,message,from_email,com_email)
    return JsonResponse({"context":"Thanks for we will soon get in touch with you"})
