from django.shortcuts import render
from dogdog.models import *

def index(request):
  return render(request, "index.html")

def addUser(request):
  if request.is_ajax() and request.POST:
    Title = request.POST.get('Title')
    Description = request.POST.get('Description')
    StartDate = request.POST.get('StartDate')
    EndDate = request.POST.get('EndDate')
    Category = request.POST.get('Category')

    event = Event(Title=Title, Description=Description, StartDate=StartDate, EndDate=EndDate, Category=Category)
    event.save()

    return HttpResponse("", content_type='application/json')

def deleteUser(request):
  if request.is_ajax() and request.POST:
    Title = request.POST.get('id')

    Event.objects.filter(id=id)