from django.db import models

# Create your models here.

class contactus(models.Model):
    Name=models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=100,null=True)
    Mobile=models.CharField(max_length=25,null=True)
    Message=models.TextField(null=True)
    def __str__(self):
        return self.Name
class category(models.Model):
    cname=models.CharField(max_length=200,null=True)
    cpic=models.ImageField(upload_to='static/categroy/',null=True)
    cdate=models.DateField()
    
class slider(models.Model):
    spic=models.ImageField(upload_to='static/slider/',null=True)
    sdate=models.DateField()