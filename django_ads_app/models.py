from django.db import models

# Create your models here.

class Ad:
    id: int
    seller: str
    title: str
    price: float

class Category:
    id: int
    title: str
    image: object
    url: str

