from django.db import models

# Create your models here.

class Lokasi(models.Model): 
    nama=models.CharField(max_length=30,null=True)
    alamat=models.TextField(max_length=50,null=True)
    wpp=models.CharField(max_length=30,null=True)
    provinsi=models.CharField(max_length=30,null=True)
    golongan=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.nama

class Location(models.Model):
    name= models.CharField(max_length=50,null=True)
    desc= models.TextField(max_length=100,null=True)
    prov= models.CharField(max_length=30,null=True)
    pict= models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name