from django.shortcuts import render, get_object_or_404
from .models import AnimeArticles

def index(request):
    return render(request, "nobsnews/index.html")

def not_ready(request):
    return render(request, "nobsnews/not_ready.html")

def home(request):
    articles = AnimeArticles.objects.all().order_by("-date_posted")

    context = {
        'articles': articles
    }

    return render(request, "nobsnews/home.html", context)

def article_detail(request, pk):
    
    article = get_object_or_404(AnimeArticles, id=pk)

    context = {
        'article': article
    }
    
    return render(request, "nobsnews/article_detail.html", context)