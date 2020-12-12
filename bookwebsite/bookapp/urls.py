from django.urls import path
from . import views
urlpatterns=[
        path('',views.home),
        path('addbook/',views.addbooks,name='addbook'),
        path('bookworld/',views.master,name='bookworld'),
        path('booklist/',views.show_books,name='booklist'),
        path('editbook/<int:id>',views.editbook,name='editbook'),
        path('deletebook/<int:id>',views.delete_book,name='deletebook')
]