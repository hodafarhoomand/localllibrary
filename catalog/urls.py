from django.conf.urls import include, url
from . import views
app_name = 'catalog'
urlpatterns = [
    url('^$' ,  views.Index.as_view() , name = 'index'),
    url('^books/$',views.BookListView.as_view() , name = 'books'),
    url('^book/(?P<pk>\d+)/$',views.BookDetailView.as_view() , name = 'book-detail'),
    url('^authors/$' , views.AuthorListView.as_view() , name = 'authors')
]
