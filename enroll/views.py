from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
from django.http import JsonResponse


# Create your views here.

def home(request):
    form = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'home.html', {'form': form, 'stu': stud})


def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = request.POST['name']
            roll = request.POST['roll']
            mobile = request.POST['mobile']
            program = request.POST['program']
            usr = Student(name=name, roll=roll, mobile=mobile, program=program)
            usr.save()
            stud = Student.objects.values()
            student_data = list(stud)
            return JsonResponse({'status': 'Save', 'student_data': student_data})
        else:
            return JsonResponse({'status': 0})
