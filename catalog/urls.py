from django.conf.urls import include, url
from . import views
app_name = 'catalog'
urlpatterns = [
    url('^$' ,  views.Index.as_view() , name = 'index'),
    url('^books/$',views.BookListView.as_view() , name = 'books'),
    url('^book/(?P<pk>\d+)/$',views.BookDetailView.as_view() , name = 'book-detail'),
    url('^authors/$' , views.AuthorListView.as_view() , name = 'authors'),
    url('^authors/(?P<pk>\d+)/$' , views.AuthorDetailView.as_view() , name = 'author-detail'),
    url('^mybooks/$' , views.LoanedBooksByUserListView.as_view() , name = 'all_borrowd'),
    url('^book/(?P<pk>[-\w]+)/renew/$' , views.renew_book_librarian ,name = 'renew_book_librarian'),
    url('^author/(?P<pk>\d+)/update/$' , views.AuthorUpdate.as_view() , name ='author_update'),
    url('^author/(?P<pk>\d+)/delete/$' , views.AuthorDelete.as_view() , name = 'author_delete'),
    url('^author/create/$' , views.AuthorCreate.as_view() , name = 'author_create')
]
