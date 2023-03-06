from django.shortcuts import render, redirect
from .form import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})
