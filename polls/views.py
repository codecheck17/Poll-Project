from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question
def home(request):
    return HttpResponse('home page')
def detail(request,question_id):
    return HttpResponse('detail page')
def result(request,question_id):
    return HttpResponse('result page')  
def vote(request,question_id):
    return HttpResponse('vote')
def index(request):
    questions = Question.objects.get()
    return render(request,'polls/templates/index.html',questions)                  
# Create your views here.
