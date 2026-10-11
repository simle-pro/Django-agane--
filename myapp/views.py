from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import *


def group_list(request):
    groups = Group.objects.annotate(average_grade=Avg('student__grade'))
    return render(request, 'groups/group_list.html', {'groups': groups})

def group_detail(request, pk):
    try:
        group = Group.objects.annotate(average_grade=Avg('student__grade')).get(pk=pk)
        students = group.student_set.all()
    except Group.DoesNotExist:
        return redirect('group_list')
    return render(request, 'groups/group_detail.html', {'group': group, 'students': students})


def group_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room = request.POST.get('room')
        Group.objects.create(name=name, room=room)
        return redirect('group_list')
    return render(request, 'groups/group_form.html')

def group_update(request, pk):
    group = Group.objects.get(pk=pk)
    
    if request.method == 'POST':
        group.name = request.POST.get('name')
        group.room = request.POST.get('room')
        group.save()
        return redirect('group_list')
    
    return render(request, 'groups/group_form.html', {'group': group})

def group_delete(request, pk):
    try:
        group = Group.objects.get(pk=pk)
        group.delete()
    except Group.DoesNotExist:
        pass
    return redirect('group_list')



def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def student_create(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        grade = request.POST.get('grade')
        group_id = request.POST.get('group')

        group_obj = Group.objects.get(pk=group_id)

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email,
            phone=phone,
            grade=grade,
            group=group_obj
        )
        return redirect('student_list')
        
    return render(request, 'students/student_form.html', {'groups': groups})

def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    groups = Group.objects.all()

    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.grade = request.POST.get('grade')
        
        group_id = request.POST.get('group')
        student.group = Group.objects.get(pk=group_id)
        
        student.save()
        return redirect('student_list')
        
    return render(request, 'students/student_form.html', {'student': student, 'groups': groups})

def student_delete(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
    except Student.DoesNotExist:
        pass
    return redirect('student_list')