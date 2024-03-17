from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=3000)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
