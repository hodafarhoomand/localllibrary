from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date

class Genre(models.Model):
    name = models.CharField(max_length=200 )

    def __str__(self) :
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 200)
    athour = models.ForeignKey('Author', on_delete = models.SET_NULL ,null=True)
    summary = models.TextField(max_length = 1000 )
    isbn = models.CharField('ISBN' , max_length = 13)
    genre =models.ManyToManyField('Genre')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('catalog:book-detail' , args=[str(self.id)])
    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description ='Genre'

class BookInstance(models.Model) :
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    book = models.ForeignKey('Book',on_delete=models.SET_NULL ,null=True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null = True , blank = True)
    LOAN_STATUS = (
        ('m' , 'maintenance'),
        ('o', 'on loan'),
        ('a', 'available'),
        ('r', 'reseved')
    )
    status = models.CharField(max_length =1 ,choices = LOAN_STATUS , blank = True)
    borrower = models.ForeignKey(User,on_delete =models.SET_NULL,null=True ,blank=True)
    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned" , "set book as a return"),)
    def __str__(self):
        return '%s (%s)' % (self.id , self.book.title)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back :
            return True
        return False

class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null = True , blank = True)
    date_of_death = models.DateField('Died' , null = True , blank = True)

    def get_absolute_url (self) :
        return reverse('catalog:author-detail' , args=[str(self.id)])

    def __str__(self) :
        return '%s %s' % (self.last_name , self.first_name)
