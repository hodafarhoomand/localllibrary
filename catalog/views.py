from django.shortcuts import render
from . import models

def index(request) :
    num_books = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    num_intances_available = models.BookInstance.objects.filter(LOAN_STATUS = 'a' ).count()
    num_authors = models.Athour.objects.count()

    return render(request,'catalog/index.html',
        context = {
            'num_books' : num_books ,
            'num_instances' : num_instances ,
            'num_intances_available' : num_intances_available,
            'num_authors' : num_authors
        }
    )
