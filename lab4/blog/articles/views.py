from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from articles.models import Article


def archive(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()
    return render(request, "archive.html", {"posts": articles})


def get_article(request: HttpRequest, article_id: int) -> HttpResponse:
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist as err:
        msg = "Article not found"
        raise Http404(msg) from err
    else:
        return render(request, "article.html", {"post": article})
