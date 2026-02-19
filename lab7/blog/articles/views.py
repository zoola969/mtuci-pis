from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render

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


def create_post(request: HttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        msg = "Только авторизованные пользователи могут создавать статьи"
        raise Http404(msg)

    if request.method == "GET":
        return render(request, "create_post.html", {})

    if request.method == "POST":
        form = {"title": request.POST.get("title"), "text": request.POST.get("text")}
        if form["title"] and form["text"]:
            if Article.objects.filter(title=form["title"]).exists():
                form["error"] = "Статья с таким названием уже существует"  # noqa: RUF001
                return render(request, "create_post.html", {"form": form})

            article = Article.objects.create(author=request.user, title=form["title"], text=form["text"])
            return redirect("get_article", article_id=article.pk)

        form["error"] = "Не все поля заполнены"  # noqa: RUF001
        return render(request, "create_post.html", {"form": form})

    msg = "Invalid request method"
    raise Http404(msg)


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "register.html", {})

    if request.method == "POST":
        form = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
        }

        if form["username"] and form["password"]:
            if User.objects.filter(username=form["username"]).exists():
                form["error"] = "Пользователь с таким именем уже существует"  # noqa: RUF001
                return render(request, "register.html", {"form": form})

            user = User.objects.create_user(username=form["username"], email=form["email"], password=form["password"])
            login(request, user)
            return redirect("archive")

        form["error"] = "Не все поля заполнены"  # noqa: RUF001
        return render(request, "register.html", {"form": form})

    msg = "Invalid request method"
    raise Http404(msg)


def auth(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "login.html", {})

    if request.method == "POST":
        form = {"username": request.POST.get("username"), "password": request.POST.get("password")}

        if form["username"] and form["password"]:
            user = authenticate(username=form["username"], password=form["password"])
            if user is not None:
                login(request, user)
                return redirect("archive")
            form["error"] = "Неверный логин или пароль"
            return render(request, "login.html", {"form": form})

        form["error"] = "Не все поля заполнены"  # noqa: RUF001
        return render(request, "login.html", {"form": form})

    msg = "Invalid request method"
    raise Http404(msg)


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("archive")
