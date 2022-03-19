from django.shortcuts import render, redirect
from .models import studentDB
from .forms import studentForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def details(request):
    all_data = studentDB.objects.all
    return render(request, 'StudentDetails.html',{'details':all_data})

def add_student(request):
    if request.method=='POST':
        form = studentForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Student Details Added  Successfully!'))
            return redirect('StudentDetails')
    else:
        form=studentForm()
        return render(request, 'add_student.html',{'form':form})

def view_details(request, task_id):
    data = studentDB.objects.get(pk=task_id)
    return render(request, 'view.html', {'data':data})

def add_mark(request, task_id):
    if request.method == 'POST':
        task = studentDB.objects.get(pk=task_id)
        form = studentForm(request.POST or None, instance=task)
        if form.is_valid():
            mark = form.cleaned_data['marks']
            print(mark)
            if(mark>=91 and mark<=100):
                grade = 'S'
            elif(mark>=81 and mark<=90):
                grade = 'A'
            elif(mark >= 71 and mark <= 80):
                grade = 'B'
            elif(mark >= 61 and mark <= 70):
                grade = 'C'
            elif(mark >=51 and mark <= 60):
                grade = 'D'
            elif(mark>=55 and mark<=50):
                grade = 'E'
            else:
                grade = 'F'
            print(grade)
            form.save()
            task.grade = grade
            task.save()
            messages.success(request,("Mark Added!"))
            return redirect('StudentDetails')
    else:
        task = studentDB.objects.get(pk=task_id)
        return render(request, 'add_marks.html',{'task':task})


def result(request):
    fail = studentDB.objects.filter(grade='F').count()
    pas = studentDB.objects.count()
    a = pas-fail
    res = format((a/pas)*100,'.2f')
    print(res)
    return render(request, 'result.html', {'res':res})