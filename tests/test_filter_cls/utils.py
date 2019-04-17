from __future__ import unicode_literals

from tests.dj_rf.models import Book

book_qs = Book.objects.order_by('id')


def create_books(count=2):
    Book.objects.bulk_create([Book() for _ in range(count)])
    books = list(book_qs)
    return books