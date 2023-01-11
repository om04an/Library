from django.shortcuts import render
from .models import Book
import datetime


def home(request):
    books = _query_all_books_from_database()
    books_static = _number_of_books_for_certain_periods(books)

    return render(request, 'library/home.html', {'books': books,
                                                 'books_month': books_static[0],
                                                 'books_6_month': books_static[1],
                                                 'books_year': books_static[2],
                                                 'books_all_time': books_static[3]
                                                 })


def _query_all_books_from_database():
    """ Получение всех книг из БД """

    books = Book.objects.all()
    return books


def _number_of_books_for_certain_periods(books):
    """Статистика по кол-ву прочитанных книг за определенные периоды """

    today = datetime.date.today()

    if today.month <= 6:
        month = 1
    else:
        month = today.month - 6

    list_of_book_statistics = [Book.objects.filter(date__month=today.month).count(),
                               Book.objects.filter(date__range=[f"{today.year}-{month}-01",
                                                                f"{today.year}-{today.month}-{today.day}"]).count(),
                               Book.objects.filter(date__year=today.year).count(),
                               books.count()]

    return list_of_book_statistics
