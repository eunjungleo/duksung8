from django.db import models
from django.conf import settings

class Question(models.Model):
    body = models.TextField(max_length=10000)
    password = models.CharField(max_length=20)
    # public or secret
    public = models.BooleanField()
    datetime = models.DateTimeField(auto_now_add=True)
    answer = models.ForeignKey('Answer', related_name='answer', on_delete=models.PROTECT, default='큰사자가 답변을 달러 뛰어오고 있습니다. 잠시만 기다려 주세요.')

class Answer(models.Model):
    question = models.ForeignKey('Question', related_name='question', on_delete=models.PROTECT)
    datetime = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=10000)
