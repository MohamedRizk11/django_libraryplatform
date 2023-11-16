import os
import django
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
sys.path.append("D:\\libraryplatform\\src")
django.setup()
import random
from django.conf import settings
from faker import Faker
from library.models import Book, Author, Review



def create_books(n):
    fake = Faker()
    images=['1.jpg','2.jpg','3.jpg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.png']
    for _ in range(n):
        author = Author.objects.order_by('?').first()
        review = Review.objects.order_by('?').first()
        Book.objects.create(
            title=fake.sentence(),
            author=author,
            review=review,
            publication_date=fake.date_time_between(start_date='-1y', end_date='now'),
            price=random.randint(1010, 2600),
            logo=f"books/{images[random.randint(0,9)]}"
        )

def create_authors(n):
    fake = Faker()
    images=['1.jpg','2.jpeg','3.jpeg','4.jpg','5%2C,jpeg','5.jpg','6_H0vd9lD','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg']
    for _ in range(n):
        books = Book.objects.order_by('?').first()

        Author.objects.create(
            books=books,
            name=fake.name(),
            birth_date=fake.date_of_birth(),
            biography=fake.paragraph(),
            image=f"image/{images[random.randint(0,13)]}"
        )

def create_reviews(n):
    fake = Faker()
    for _ in range(n):
        
        Review.objects.create(
            reviewer_name=fake.name(),
            content=fake.paragraph(),
            rating=fake.random_int(min=0, max=5),
              # Set the review from the Book side
        )


# Usage examples:
create_authors(1500)
create_books(2000)
create_reviews(2000)
