from django.urls import path
from . import views
urlpatterns = [
    path('books/', views.Book_post.as_view(), name='book_post_page'),

    path('book_detail/<int:id>', views.BookDetailsPost.as_view(), name='book_detail_page'),

    path('borrow/<int:id>/', views.BorrowBook, name='borrow_book_page'),

    path('return/<int:id>/', views.ReturnBook, name='return_book_page'),
]
