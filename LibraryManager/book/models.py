from django.db import models

# book object
class Book(models.Model):
    bookID = models.CharField(unique=True, max_length=50)
    name   = models.CharField(max_length=100)
    isIssued = models.BooleanField(default=False)

    def __str__(self):
        return self.bookID

# access request object
class AccessReq(models.Model):
    bookID = models.CharField(max_length=50)
    studID = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)
