from typing import override

from django.contrib.auth.models import User
from django.db import models

_MAX_EXCERPT_LENGTH = 140


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    @override
    def __str__(self) -> str:
        return f"{self.author.username}: {self.title}"

    def get_excerpt(self) -> str:
        return self.text[:_MAX_EXCERPT_LENGTH] + ("..." if len(self.text) > _MAX_EXCERPT_LENGTH else "")
