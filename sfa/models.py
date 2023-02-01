from django.db import models

class Player2(models.Model):
    name=models.CharField( max_length=100)
    mobile=models.CharField( max_length=12)
    email=models.EmailField( max_length=254)
    address=models.CharField( max_length=100)
    photo=models.ImageField(  blank=True,null=True)

    def __str__(self):
        return self.name

# class Player2(models.Model):
#     name=models.CharField( max_length=100)
#     mobile=models.CharField( max_length=12)
#     email=models.EmailField( max_length=254)
#     address=models.CharField( max_length=100)
#     photo=models.ImageField( upload_to="/player",  blank=True,null=True)

#     def __str__(self):
#         return self.name