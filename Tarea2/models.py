from django.db import models

# Create your models here.
class RazonSocial(models.Model):
  id_sanionatorio = models.ForeignKey('Sancionatorios', on_delete=models.CASCADE)
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
class Categoria(models.Model):
  id_sanionatorio = models.ForeignKey('Sancionatorios', on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
  
class Fiscalizacion(models.Model):
  id_sanionatorio = models.ForeignKey('Sancionatorios', on_delete=models.CASCADE)
  name = models.CharField(max_length=150)
  
  def __str__(self):
    return self.name
  
class Sancionatorios(models.Model):
  expediente = models.CharField(max_length=150, primary_key=True)
  region = models.CharField(max_length=100)
  estado = models.CharField(max_length=100)
  link = models.CharField(max_length=100, null=True)
  
  def get_categoria_names(self):
    return [categoria.name for categoria in Categoria.objects.filter(id_sanionatorio=self)]   
  
  def __str__(self) -> str:
    return f'{self.expediente} - {self.estado}'
  