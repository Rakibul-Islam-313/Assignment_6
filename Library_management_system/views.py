from django.shortcuts import render
from Books.models import Books
from book_category.models import Categories

def home(request, category_slug = None):
    data = Books.objects.all()
    book_category = Categories.objects.all()

    if category_slug is not None:
        category = Categories.objects.get(slug = category_slug)
        data = Books.objects.filter(categories = category)

    return render(request, 'home.html', {'data': data, 'book_category': book_category})
