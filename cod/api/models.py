from django.db import models

from registration.models import MyUser

class Quiz(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    start = models.DateField(auto_now_add=True)
    end = models.DateField()

    def __str__(self):
        return self.title


QUESTION_TYPES = (
    ('text answer', 'text'),
    ('one answer', 'one'),
    ('multiple answer', 'multiple'),
)


class Question(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=80, choices=QUESTION_TYPES)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, related_name='questions')

    def __str__(self):
        return self.title


class Choice(models.Model):
    title = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text_answer = models.TextField(null=True, blank=True)
    one_answer = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, related_name='one_answer', blank=True)
    multiple_answers = models.ManyToManyField(Choice, null=True, blank=True)

    def __str__(self):
        return str(self.question)
