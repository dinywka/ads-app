from django.db import models

# Create your models here.

class Ad:
    id: int
    seller: str
    title: str
    price: float
