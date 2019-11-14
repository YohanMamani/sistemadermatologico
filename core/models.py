from django.db import models

# Create your models here.

class paciente(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=300, blank= True, null= True)
    apellidos= models.CharField(max_length=300, blank= True, null= True)
    DNI= models.CharField(max_length=300, blank= True, null= True)
    historia= models.CharField(max_length=300, blank= True, null= True)
    imagen= models.CharField(max_length=300, blank= True, null= True)
    doctor= models.CharField(max_length=300, blank= True, null= True)