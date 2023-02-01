from django.db import models

# Create your models here.


class Player(models.Model):
    name=models.CharField( max_length=100)
    mobile=models.CharField( max_length=12)
    email=models.EmailField( max_length=254)
    address=models.CharField( max_length=100)
    photo=models.ImageField( upload_to="player/",  blank=True,null=True)

    def __str__(self):
        return self.name