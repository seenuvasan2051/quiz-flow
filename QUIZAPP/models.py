from django.db import models

class user(models.Model):
    name = models.CharField(max_length = 25)
    address = models.CharField(max_length = 25)
    email = models.CharField(max_length = 25)
    phonenumber = models.CharField(max_length = 25)
    password = models.CharField(max_length = 25)
    is_active = models.IntegerField(default = 1)

class Quiz(models.Model):
    QUIZ_TYPES = [
        ('maths', 'Maths'),
        ('english', 'English'),
        ('gk', 'General Knowledge'),
    ]

    quiz_type = models.CharField(max_length=255, choices=QUIZ_TYPES, null=True, default=None)
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)
