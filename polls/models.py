from django.db import models

# These models give Django lots of informations and the ability to do:
# 1. Create a database schema (CREATE TABLE statements) for the app
# 2. Create a Python database-access API for accessing Question & Choice objects

# Include the "polls" app to the project in ../mysite/settings.py
# - reference it by adding PollsConfig in the ./polls/apps file in the INSTALLED_APPS section

# Then run "python manage.py makemigrations polls" 
# Followed by "python manage.py migrate"

# We run makemigrations to tell Django that we've made changes to models / added models 
# - and that we would like the changes to be strored as a migration
# Migrations are how Django stores changes to models (and thus our DB schema) -- they're files on disk

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # ForeignKey tells Django that each Choice is related to a single Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
