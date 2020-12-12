from django.db import models

# Create your models here.\

class Publisher(models.Model):
    name=models.CharField(max_length=30)
    website=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return f"{self.name}"


class Books(models.Model):
    book_title=models.CharField(max_length=50)
    author=models.CharField(max_length=60)
    price=models.IntegerField()
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.id}- {self.book_title}-{self.author}-{self.price}-{self.publisher}"



