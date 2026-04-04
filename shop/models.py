from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    def __str__(self):
        return self.brand_name

class Size(models.Model):
    size = models.CharField(max_length=35)
    def __str__(self):
        return self.size
    
class Color(models.Model):
    color = models.CharField(max_length=30)
    def __str__(self):
        return self.color
    
class Clothes(models.Model):
    title = models.CharField(max_length=300)
    Brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    description = models.TextField()
    image = models.ImageField(upload_to='photos')
    image2 = models.ImageField(upload_to='photos', null=True, blank=True)
    image3 = models.ImageField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return self.title