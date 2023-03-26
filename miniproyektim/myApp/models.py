from django.db import models

# Create your models here.
class Harflar(models.Model):
    #id1 = models.TextField(verbose_name='id')
    name = models.CharField(max_length=100,verbose_name="So'z")
    uploaded_file = models.FileField(verbose_name='ovoz')
    photo = models.ImageField(verbose_name='Rasm')
    #description = models.TextField() 

    def __str__(self) -> str:
        return self.name

