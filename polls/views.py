from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views / pages here.

# Django render looks for templates from the "./templates" folder within polls
# - so we have to supply the path from within "./templates" that we want to render
# The default path it looks for is "templates" but we can change that from settings.py of our "mysites" app

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("You're look at the results of question {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))

