from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from articles.models import Article


def archive(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()
    return render(request, "archive.html", {"posts": articles})
