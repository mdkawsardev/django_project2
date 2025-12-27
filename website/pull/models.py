from django.db import models

# Create your models here.
class questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

class choice(models.Model):
    question = models.ForeignKey(questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)