import uuid
from django.db import models

class Question(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
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