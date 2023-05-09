from django.http import HttpResponse
from django.template import loader
from .models import Student
from django.db.models import Q
from django.shortcuts import render


def students(request):
    mystudents = Student.objects.all().values()
    template = loader.get_template('all_students.html')
    context = {
        'mystudents': mystudents,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mystudent = Student.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mystudent': mystudent,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))


def link1(request):
    template = loader.get_template('link1.html')
    return HttpResponse(template.render())


def link2(request):
    template = loader.get_template('link2.html')
    return HttpResponse(template.render())


def link3(request):
    template = loader.get_template('link3.html')
    return HttpResponse(template.render())


def index(request):
    if request.method == "GET":
      if 'q' in request.GET:
          q = request.GET['q']
          # data = Data.objects.filter(first_name__icontains=q)
          multiple_q = Q(Q(firstname__icontains=q) | Q(lastname__icontains=q))
          student = Student.objects.filter(multiple_q)
      else:
         student = Student.objects.all()
      context = {
        'student': student,
        'q':q
      }
    # template = loader.get_template('index.html')
    # return HttpResponse(request, template.render(), context)
    return render(request, 'index.html', context)
