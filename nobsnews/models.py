from django.db import models
from ckeditor.fields import RichTextField

class AnimeArticles(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    snippet = models.TextField(default="thi is some default text")
    header_img = models.ImageField(upload_to='header_imgs/')
    body = RichTextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
