import uuid
from django.db import models

# Roles
# Name(optional)
class Question(models.Model):
    id = models.AutoField(primary_key = True, editable = False)
    question_text = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=500)
    cost = models.DecimalField("amount charged", decimal_places=4, max_digits=8)
    tokens = models.IntegerField("tokens generated")

    def __str__(self) -> str:
        return self.answer_text