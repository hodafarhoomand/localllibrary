from django.conf.urls import include, url
from . import views
app_name = 'catalog'
urlpatterns = [
    url('^s' ,  views.index , name = 'index'),
]
