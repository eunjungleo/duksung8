from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from .models import Question, Answer

class MainView(TemplateView):
    template_name = "main.html"

class QnaListView(ListView):
    model = Question
    template_name = "qna.html"

class QnaCreateView(CreateView):
    model = Question
    template_name = "ask.html"

class QnaCheckView(DetailView):
    model = Question
    template_name = 'qnacheck.html'

class AboutView(TemplateView):
    template_name = "about.html"

class PastView(TemplateView):
    template_name = "2019.html"

class ScheduleView(TemplateView):
    template_name = "2020.html"

class PeopleView(TemplateView):
    template_name = "2019.html"

