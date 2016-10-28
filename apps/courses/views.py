from django.shortcuts import render, redirect, reverse
from models import Courses, Descriptions

# Create your views here.
def index(request):
    show_data = Descriptions.objects.select_related()
    print "Here is data!", show_data
    context = {'data': show_data}
    print show_data.query
    return render(request,
    'courses/index.html', context)

def add(request):
    if request.method == 'POST':
        course_name = request.POST['name']
        description_post = request.POST['description']
        if course_name == "" or description_post == "":
            return redirect('/')
        c = Courses(name = course_name)
        c.save()
        d = Descriptions(description = description_post, course = c)
        d.save()
    return redirect(reverse('main'))

def remove(request, course_id):
    if request.method == "GET":
        show_data = Descriptions.objects.get(course = course_id)
        print id, "get request"
        context = {"course_id": course_id,
                   "data": show_data}
        return render(request,
        'courses/remove.html', context)
    elif request.method == "POST":
        c = Courses.objects.get(id = course_id)
        d = Descriptions.objects.get(course = c)
        d.delete()
        c.delete()
        print c
        print d
        print course_id, "POST request"
        return redirect(reverse('main'))
