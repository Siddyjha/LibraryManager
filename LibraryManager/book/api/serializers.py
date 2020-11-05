from rest_framework import serializers
from book.models import Book, AccessReq

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bookID','name', 'isIssued']

class AccReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessReq
        fields = ['bookID', 'studID']