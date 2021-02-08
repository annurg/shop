from django.shortcuts import render
from .models import Item, Record, Person
# Create your views here.


def home(request):
    pass

def book(request):
    book = Person.objects.all()
    render(request, '/khatabook/book.html', {'book': book})