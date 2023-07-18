from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    '''The book that a user will discuss in their journal entry'''
    text = models.CharField(max_length=200)
    entry_date = models.DateTimeField(auto_now_add=True) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''This method returns the string from of the model'''
        return self.text

class Entry(models.Model):
    '''A user's journal entry on a specific book'''
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        '''This method returns the first 50 characters of 
        a string representing the entry'''
        return f"{self.text[:50]}..."