from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Book, Entry
from .forms import BookForm, EntryForm

# Create your views here.

def index(request):
    '''Bookworm's home page'''
    return render(request, 'bookworm/index.html')

@login_required
def books(request):
    '''Displays the list of books'''
    books = Book.objects.filter(owner=request.user).order_by('entry_date')
    context = {'books': books}
    
    return render(request, 'bookworm/books.html', context)

@login_required
def book(request, book_id):
    '''Displays the entry details for a book'''
    book = Book.objects.get(id=book_id)

    if book.owner != request.user:
        raise Http404
    
    entries = book.entry_set.order_by('-entry_date')
    context = {'book': book, 'entries': entries}

    return render(request, 'bookworm/book.html', context)

@login_required
def new_book(request):
    '''Adds a new book'''
    if request.method != 'POST':
        #If no data is submitted, a blank form is created
        form = BookForm()
    
    else:
        #Processing of the submitted data
        form = BookForm(data=request.POST)
        
        #Check against incorrect and malicious data
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.owner = request.user
            new_book.save()

            return redirect('bookworm:books')
        
    context = {'form': form}
    
    return render(request, 'bookworm/new_book.html', context)

@login_required
def new_entry(request, book_id):
    '''Adds a new entry'''
    book = Book.objects.get(id=book_id)

    if request.method != 'POST':
        #If no data is submitted, a blank form is created
        form = EntryForm()
    
    else:
        #Processing of the submitted data
        form = EntryForm(data=request.POST)
        
        #Check against incorrect and malicious data
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.book = book
            form.save()

            return redirect('bookworm:book', book_id=book_id)
        
    context = {'book': book, 'form': form}
    
    return render(request, 'bookworm/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    '''Edits a previous entry'''
    entry = Entry.objects.get(id=entry_id)
    book = entry.book

    if book.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    
    else:
        #Processing of the submitted data
        form = EntryForm(instance=entry, data=request.POST)
        
        #Check against incorrect and malicious data
        if form.is_valid():
            form.save()

            return redirect('bookworm:book', book_id=book.id)
        
    context = {'entry': entry, 'book': book, 'form': form}
    
    return render(request, 'bookworm/edit_entry.html', context)