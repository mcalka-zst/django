from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Category


def index(request):
    # allbooks = Books.objects.all()  # to samo co SELECT * FROM Books
    # first = Books.objects.get(pk=1)  # primary key =1
    # history = Books.objects.filter(category_id=2)
    # rebis = Books.objects.filter(publishingHouse_id=3)
    # null = Books.objects.filter(category_id__isnull=True)
    # ijon = Books.objects.filter(description__contains='Ijon Tichy')
    categories = Category.objects.all()
    data = {'categories': categories}
    return render(request, 'template.html', data)


def category(request, id):
    onecategory = Category.objects.get(pk=id)
    book_category = Books.objects.filter(category_id=onecategory)
    categories = Category.objects.all()
    data = {'onecategory': onecategory,
            'book_category': book_category,
            'categories': categories}
    return render(request,'book_category.html', data)


def title(request, id):
    onetitle = Books.objects.get(pk=id)
    return HttpResponse(onetitle.title)


def book(request, id):
    onebook = Books.objects.get(pk=id)
    categories = Category.objects.all()
    data = {'onebook': onebook, 'categories': categories}
    return render(request, 'book.html', data)  # przekazujemy słownik data do book.html
