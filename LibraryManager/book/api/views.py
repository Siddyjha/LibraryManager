from book.api.serializers import BookSerializer, AccReqSerializer
from book.models import Book, AccessReq

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


"""
API for Student
"""

# List all available books in library
@api_view(['GET',])
def getAvailableBooks(request):
    books = Book.objects.all().filter(isIssued=False)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# Issue Book
@csrf_exempt
@api_view(['POST',])
def issueBook(request):

    student_id = request.data.get('studID')
    book_id = request.data.get('bookID')

    try:
        book = Book.objects.get(bookID=book_id)
    except Book.DoesNotExist:
        return Response({"message":"Book does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    if(book.isIssued == True):
        return Response({"message":"Book is already Issued, request access from librarian"})
    else:
        book.isIssued = True
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

# return book
@csrf_exempt
@api_view(['POST',])
def returnBook(request):
    
    book_id = request.data.get('bookID')

    try:
        book = Book.objects.get(bookID=book_id)
    except Book.DoesNotExist:
        return Response({"message":"Book does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    if(book.isIssued == False):
        return Response({"message":"Book is not yet Issued, cannot return"})
    else:
        book.isIssued = False
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

# Request Access
@csrf_exempt
@api_view(['POST',])
def reqAccess(request):
    
    student_id = request.data.get('studID')
    book_id = request.data.get('bookID')
    
    try:
        book = Book.objects.get(bookID=book_id)
    except Book.DoesNotExist:
        return Response({"message":"Book does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
    if(book.isIssued == False):
        return Response({"message":"Book is already available to be issued"})
    else:
        serializer = AccReqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)


"""
API for Librarian
"""
# Get all books in the library
@api_view(['GET',])
def getAllBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# Get all access requests
@api_view(['GET',])
def getAccessReq(request):
    req = AccessReq.objects.all()
    serializer = AccReqSerializer(req, many=True)
    return Response(serializer.data)
