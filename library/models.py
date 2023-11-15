from datetime import date
from pickle import TRUE
from django.utils import timezone
from tkinter import CASCADE
from django.db import models
from django.utils.text import slugify


# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=50)
    birth_date=models.DateField()
    biography=models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image', default='1.jpg')
    slug=models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
       self.slug=slugify(self.name)
       super(Author, self).save(*args, **kwargs) 

class Book(models.Model):
    title =models.CharField(max_length=100)
    author=models.ForeignKey('Author',on_delete=models.CASCADE,related_name='book_author')
    publication_date=models.DateTimeField(default=timezone.now)
    price=models.IntegerField(null=True,blank=True)
    logo=models.ImageField(upload_to='books')
    review = models.ForeignKey('Review', on_delete=models.CASCADE,related_name='book_review')

    slug=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
       self.slug=slugify(self.title)
       super(Book, self).save(*args, **kwargs) 

class Review(models.Model):
    reviewer_name= models.CharField(max_length=50)
    content =models.TextField(max_length=1000)
    rating_choices = [(i, str(i)) for i in range(6)]  # Choices from 0 to 5
    rating = models.IntegerField(choices=rating_choices, default=0)

    def __str__(self):
        return self.reviewer_name

