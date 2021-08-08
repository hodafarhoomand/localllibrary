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
class BookInstance(models.Models) :
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    book = models.ForeigKey('Book',on_delete=models.SET_NULL ,null=True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null = True , Blank = True)
    LOAN_STATUS = (
        ('m' , 'maintenance'),
        ('o', 'on loan'),
        ('a', 'available'),
        ('r', 'reseved')
    )
    status = models.Charfield(max_length =1 ,choices = LOAN_STATUS , blank = True)
    class Meta:
        ordering = ['due_back']
    def __str__(self):
        return '%s (%s)' % (self.id , self.book.title)

class Author(models.Model):
    first_name = models.Charfield(max_lenth = 100)
    last_name = models.Charfield(max_lenth = 100)
    date_of_birth = models.DateField(null = True , blank = True)
    date_of_death = models.DateField('Died' , null = True , blank = True)

    def get_absolute_url (self) :
        return reverse('Athour-detail' , args=[str(self.id)])

    def __str__(self) :
        return '%s %S' % (self.last_name , self.first_name)
