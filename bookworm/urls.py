from django.urls import path
from .import views

app_name = "bookworm"

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page containing the list of books
    path('books/', views.books, name='books'),
    #Page with entry details for a book
    path('books/<int:book_id>/', views.book, name='book'),
    #Page for users to add a new book
    path('new_book/', views.new_book, name='new_book'),
    #Page for adding a new entry
    path('new_entry/<int:book_id>/', views.new_entry, name='new_entry'),
    #Page for editing a previous entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]