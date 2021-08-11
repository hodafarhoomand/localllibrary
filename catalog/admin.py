from django.contrib import admin
from . import models

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status','due_back','borrower')
    fieldsets =(
        (None,{ 'fields' : ('book' , 'imprint', 'id') }) ,
        ('availability' , {'fields' : ('status' , 'due_back','borrower')})
    )

class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' ,'athour','display_genre')
    inlines = [BookInstanceInline]

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name' , 'first_name' , 'date_of_birth' , 'date_of_death')
    fields = ['last_name' , 'first_name',('date_of_birth' , 'date_of_death')]

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
