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
    question_text = models.CharField(max_length=256, blank=True)
    type = models.CharField(max_length=11, choices=Type.choices, default=Type.TEXT)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=255, blank=True)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, null=False, blank=False)
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return str(self.choice_text)


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=False)
    date_reply = models.DateTimeField(auto_now_add=True, editable=False, null=False)

    def __str__(self):
        return f'{self.poll}.  {self.user}'


class Answer(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    reply = models.ForeignKey(Reply, related_name='answers', on_delete=models.CASCADE, null=False)

    def __str__(self):
        if self.text:
            return self.text
        elif self.choice.choice_text:
            return self.choice.choice_text
