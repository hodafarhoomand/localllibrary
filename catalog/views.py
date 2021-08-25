from django.shortcuts import render , get_object_or_404
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse 
from django.urls import reverse_lazy
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
class AuthorDetailView(generic.DetailView):
    model = models.Author
    template_name = 'catalog/author_detail.html'
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


#@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request,pk):
    book_inst = get_object_or_404(models.BookInstance , pk = pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()
            return HttpResponseRedirect(reverse('catalog:all_borrowd'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks = 3)
        form = RenewBookForm(initial={'renewal_date' : proposed_renewal_date})
    return render (request , 'catalog/book_renew_librarian.html' ,{'form' : form , 'bookinst' : book_inst})

class AuthorCreate(generic.CreateView):
    model = models.Author
    fields = "__all__"
    initial = {'date_of_death' : '05/12/2021'}

class AuthorUpdate(generic.UpdateView):
    model = models.Author
    fields = ['first_name' , 'last_name' , 'date_of_birth' , 'date_of_death']

class AuthorDelete(generic.DeleteView) :
    model = models.Author
    success_url = reverse_lazy('catalog:authors')


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
