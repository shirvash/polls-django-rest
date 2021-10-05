from django import utils
from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    title = models.CharField(max_length=63)
    date_start = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    date_end = models.DateTimeField()
    description = models.TextField(max_length=255, blank=True)

    @property
    def is_active(self):
        if self.date_end:
            return self.date_end > utils.timezone.now()
        return False

    def __str__(self):
        return f'{self.pk}. {self.title}   ({self.date_start.year})'


class Question(models.Model):
    class Type:
        TEXT = 'TEXT'
        CHOICE = 'CHOICE'
        MULTICHOICE = 'MULTICHOICE'

        choices = (
            (TEXT, 'TEXT'),
            (CHOICE, 'CHOICE'),
            (MULTICHOICE, 'MULTICHOICE'),
        )

    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE, null=False, blank=False)
    text = models.CharField(max_length=256)
    type = models.CharField(max_length=11, choices=Type.choices, default=Type.TEXT)

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, null=False, blank=False)
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.text


class Complete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=False)
    date_complete = models.DateTimeField(auto_now_add=True, editable=False, null=False)


class Answer(models.Model):
    text = models.CharField(max_length=255)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    complete = models.ForeignKey(Complete, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        if self.text:
            return self.text
        elif self.choice:
            return self.choice
