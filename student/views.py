from django.shortcuts import render,redirect
from student.models import Student
# Create your views here.
def home(request):
    student=Student.objects.all()

    return render(request,"student/home.html",{'student':student})
def add_student(request):
    if request.method=="POST":
       print("Added")
       stds_roll=request.POST.get("std_roll")
       stds_name=request.POST.get("std_name")
       stds_email=request.POST.get("std_email")
       stds_address=request.POST.get("std_address")
       stds_phone=request.POST.get("std_phone")
       
       s=Student()
       s.roll=stds_roll
       s.name=stds_name
       s.email=stds_email
       s.address=stds_address
       s.phone=stds_phone

       s.save()
       return redirect("/student/home")

    return render(request,"student/add_student.html",{})
def delete_student(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect("/student/home")
def update_student(request,roll):
    student=Student.objects.get(pk=roll)
    return render(request,"student/update_student.html",{'student':student})
def do_update_student(request,roll):
    if request.method=="POST":
        student_roll=request.POST.get("student_roll")
        student_name=request.POST.get("student_name")
        student_email=request.POST.get("student_email")
        student_address=request.POST.get("student_address")
        student_phone=request.POST.get("student_phone")

        student=Student.objects.get(pk=roll)
        student.roll=student_roll
        student.name=student_name
        student.email=student_email
        student.address=student_address
        student.phone=student_phone
        student.save()
        return redirect("/student/home")
    return render (request,"student/update_student.html",{})
    
