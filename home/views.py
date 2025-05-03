from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')


def about(request):
   return render(request, 'home/about.html')

def booking(request):
    return render(request, 'home/booking.html')

def doctors(request):
   return render(request, 'home/doctors.html')

def contact(request):
    return render(request, 'home/contact.html')

def department(request):
    return render(request, 'home/department.html')