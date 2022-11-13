from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

estado =[
    ('Recibido por Conserje', 'Recibido por Conserje'),
    ('Entregado', 'Entregado')
]

class residencia(models.Model):
    numero= models.IntegerField()
    dueño= models.CharField(max_length=50)
    telefono= models.CharField(max_length=9)
    mail= models.EmailField(max_length=254)
    
    def __str__(self):
        return self.numero

class correspondencia(models.Model):
    fecha_recepcion=models.DateField(default=timezone.now)
    conserje=models.CharField(max_length=50)
    remitente=models.CharField(max_length=50)
    destinatario=models.CharField(max_length=50)
    estado=models.CharField(choices=estado, max_length=50)
    nro_residencia=models.ForeignKey(residencia, on_delete=models.CASCADE)

