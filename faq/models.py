from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=200, unique=True)
    answer = models.CharField(max_length=500)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return {self.question}