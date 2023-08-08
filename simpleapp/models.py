from django.db import models
from django.utils import timezone



class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    NEWS = "NW"
    ARTICLE = "AR"
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )

    description = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',
    )
    #dateCreation = models.DateTimeField(auto_now=True)
    dateCreation = models.DateField(default=timezone.now)


    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()