from django.db import models

class Categoria(models.Model):
    sku = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    img = models.ImageField(upload_to="imagenes_categoria", null=True, blank=True)

    def __str__(self):
        txt="[0] {1}"
        return txt.format(self.sku,self.nombre)

class Producto(models.Model):
    sku = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField(null=False,default=0)
    stock = models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    img = models.ImageField(upload_to="imagenes_producto")

    def __str__(self):
        txt="[0] {1} {2}"
        return txt.format(self.sku,self.descripcion,self.nombre)

    
class Usuario(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50,null=False, primary_key=True)
    gmail = models.CharField(max_length=50,null=False,unique=True)
    password = models.CharField(max_length=50,null=False,unique=True)

    def __str__(self):
        txt="[0] {1}"
        return txt.format(self.username,self.nombre)


