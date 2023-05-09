import datetime

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
    description: str
    date_created: datetime.datetime
    date_updated: datetime.datetime
    health: bool
    location: str
    category: str
    rating: object
    comments: object

