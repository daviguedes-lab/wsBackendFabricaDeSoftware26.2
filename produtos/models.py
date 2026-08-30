from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Pizza(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='pizzas/', blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="pizzas"
    )

    def __str__(self):
        return self.nome