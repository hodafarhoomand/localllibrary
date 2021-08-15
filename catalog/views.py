from django.shortcuts import render , get_objects_or_404
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponeRedirect
from django.core.urlresolvers import reverse
import datetime
from .forms import RenewBookForm

class Index(generic.TemplateView) :
    template_name = 'catalog/index.html'
    def get_context_data (self,**kwargs) :
        context = super().get_context_data(**kwargs)
        context['num_books'] = models.Book.objects.all().count()
        context['num_instances'] = models.BookInstance.objects.all().count()
        context['num_intances_available'] = models.BookInstance.objects.filter(status__exact = 'a' ).count()
        context['num_authors'] = models.Author.objects.count()
        return context

class BookListView(generic.ListView) :
    model = models.Book
    # context of BookListView() is book_list by default
    template_name = 'catalog/book_list.html'

class BookDetailView(generic.DetailView) :
    model = models.Book
    template_name = 'catalog/book_detail.html'

class AuthorListView(generic.ListView):
    model = models.Author
    template_name = 'catalog/author_list.html'

# class MyView(LoginRequiredMixin,view):
#     login_url = '/login/'
#     required_field_name ='redirect_to'

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = models.BookInstance
    template_name = 'catalog/bookninstance_list_borrowed_user.html'
    pegindate_by = 10
    #how many records must be in each page as reault
    def get_queryset(self):
        return models.BookInstance.objects.filter(borrower=self.request.user).filter(status__exact = 'o').order_by('due_back')


@permission_required('catalog.can_mark_returned')
def renew_book_linrarian(request,pk):
    book_inst = get_objects_or_404(BookInstance , pk = pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_inst.due_back = FORM.cleaned_data['renewal_date']
            book_inst.save()
            return HttpResponeRedirect(reverse('all_borrowd'))
    else:
        proposed_renewal_date = date.datetime.today() + datetime.timedelta(weeks = 3)
        form = RenewBookForm(initial={'renewal_date' : proposed_renewal_date})
    return render (request , 'catalog/book_renew_librarian.html' ,
                    {'form' = form , 'bookinst' = book_inst})


# def index(request) :
#     num_books = models.Book.objects.all().count()
#     num_instances = models.BookInstance.objects.all().count()
#     num_intances_available = models.BookInstance.objects.filter(status__exact = 'a' ).count()
#     num_authors = models.Author.objects.count()
#
#     return render(request,'catalog/index.html',
#         context = {
#             'num_books' : num_books ,
#             'num_instances' : num_instances ,
#             'num_intances_available' : num_intances_available,
#             'num_authors' : num_authors
#         }
#     )
