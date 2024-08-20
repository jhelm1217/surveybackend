from django.db import models

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=50) 

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
