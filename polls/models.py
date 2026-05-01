from django.db import models
from django.utils import timezone


class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name="Date Published")

    def __str__(self):
        return self.question
    
    def was_currently_published(self):
        return self.pub_date <= timezone.now() - timezone.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    