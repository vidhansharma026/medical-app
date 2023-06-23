from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def index(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'registration.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = make_password(request.POST['password'])
        if Registration.objects.filter(email = email).exists():
            messages.error(request, 'email already exists')
            return redirect('/signup/')
        elif Registration.objects.filter(mobile = mobile).exists():
            messages.error(request, 'mobile already exists')
            return redirect('/signup/')
        else:
            Registration.objects.create(name = name, email = email, mobile = mobile, password = password)
            messages.success(request,'registration successful')
            return redirect('/')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if Registration.objects.filter(email = email).exists():
            reg = Registration.objects.get(email = email)
            password = reg.password
            if check_password(user_password,password):
                return redirect('/home/')
            else:
                messages.error(request,'password is incorrect')
                return redirect('/')
        else:
            messages.error(request,'email is not registered')
            return redirect('/')   

def home(request):
    doctors = Doctor.objects.all()
    gallery = Gallery.objects.all()
    return render(request, 'home.html',{'doctors': doctors, 'gallery':gallery})
       
def appoint (request):
    doctors = Doctor.objects.all()
    appointment = Appointment.objects.all()
    return render(request, 'appointment.html',{'doctors':doctors, 'appointment': appointment})

def appointment(request):
    if request.method == 'POST':
        pname = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        doctor_id = request.POST.get('doctor')
        department_id = request.POST.get('department')
        doctor = Doctor.objects.get(id = doctor_id)
        department = Doctor.objects.get(id = department_id)
        if Appointment.objects.filter(pname = pname).exists():
            messages.error(request,'appointment already exists')
        else:
            Appointment.objects.create(pname = pname, email = email, mobile = mobile, date = date, doctor = doctor, department = department)
            messages.success(request,'appointment is successfully added')
            appointment =Appointment.objects.all()
            return render(request, 'appointment.html', {'appointment': appointment})
    else:
        appointment = Appointment.objects.all()
        return render(request, 'appointment.html', {'appointment': appointment})

def msgs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msgs = request.POST['msgs']
        Msgs.objects.create(name = name, email = email, subject = subject, msgs = msgs)
        messages.success(request, 'message sent successfully')
        return redirect('/home/')
    
def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        Subscribe.objects.create(email = email)
        return redirect('/home/')
