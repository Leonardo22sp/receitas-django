# receitas/models.py

from django.db import models

class Receita(models.Model):
    CATEGORY_CHOICES = [
        ('comida', 'Comida'),
        ('sobremesa', 'Sobremesa'),
        ('drink', 'Drink'),
    ]

    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    ingredients = models.TextField(verbose_name='Ingredientes')
    instructions = models.TextField(verbose_name='Instruções')
    categoria = models.CharField( # <-- ALTERADO
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='comida', 
        verbose_name='Categoria'
    )
    image = models.ImageField(upload_to='receitas/img', blank=True, null=True, verbose_name='Imagem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ['-created_at']