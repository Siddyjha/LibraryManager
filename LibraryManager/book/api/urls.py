from django.urls import path

from book.api.views import getAvailableBooks, issueBook, reqAccess, returnBook, getAllBooks, getAccessReq

app_name = 'book'

urlpatterns = [
    # student API
    
    path('student/list', getAvailableBooks, name='list_available_books'),
    path('student/issue', issueBook, name='issue_book'),
    path('student/return', returnBook, name='return_book'),
    path('student/access_request', reqAccess, name='access_req'),

    # Librarian API

    path('librarian/list', getAllBooks, name="list_all_books"),
    path('librarian/list_access_req', getAccessReq, name="list_access_req")
]