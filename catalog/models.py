from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=200 )

    def __str__(self) :
        return self.name

        class Book(models.Model):
            title = models.CharField(max_length = 200)
            athour = models.ForeignKey('Author', on_delete=models.SET_NULL ,null=True)
            summary = models.TextField(max_length = 1000 )
            isbn = models.CharField('ISBN' , max_length = 13)
            genre =models.ManyToManyField(Genre)

            def __str__(self):
                return self.title
                def get_absolute_url():
                    return reverse('book-detail' , args=[str(self.id)])
class 
