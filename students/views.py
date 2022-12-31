from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Students
from .forms import StudentForm



def home(request):
    return render(request, 'students/index.html', {'students':Students.objects.all()})

def view_student(request,id):
    student = Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home'))

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email= form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']

            new_student = Students(
                student_number=new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study
            )

            new_student.save()
            return render(request,'students/add_student.html', {
                'form' : StudentForm(),
                'success' : True
            })

    else:
        form = StudentForm()
        return render(request, 'students/add_student.html', {
            'form' : StudentForm()
        })

def edit_student(request, id):
    if request.method == 'POST':
        student = Students.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_student.html', {
                'form' : form,
                'success' : True
            })
    else:
        student = Students.objects.get(pk=id)
        form = StudentForm(instance=student)
        return render(request, 'students/edit_student.html', {
                'form' : form
            })

def delete_student(request,id):
    student = Students.objects.get(pk=id)
    student.delete()
    return HttpResponseRedirect(reverse('home'))