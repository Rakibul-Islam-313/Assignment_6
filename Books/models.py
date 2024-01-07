from django.db import models
from book_category.models import Categories
from django.contrib.auth.models import User 
# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to = 'media/uploads/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Books, on_delete = models.CASCADE, related_name = "comments")
    name =  models.CharField(max_length = 50)
    email  = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"comment by{self.name}"

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    book = models.ForeignKey(Books, on_delete = models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.book.name}"