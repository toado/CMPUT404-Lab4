from django.db import models

# These models give Django lots of informations and the ability to do:
# 1. Create a database schema (CREATE TABLE statements) for the app
# 2. Create a Python database-access API for accessing Question & Choice objects

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # ForeignKey tells Django that each Choice is related to a single Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
