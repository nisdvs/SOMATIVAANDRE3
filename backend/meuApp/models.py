from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from meuApp.gerenciador import Gerenciador

class Usuario(AbstractBaseUser,PermissionsMixin):
    CATEGORIAS_USUARIO = (
        ('BIBLIOTECARIO', 'Bibliotecário'),
        ('AUTOR', 'Autor'),
        ('ADMIN', 'Administrador'),
        ('USUARIO', 'Usuário'),
    )

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField("endereço de email", unique=True, default='default@example.com')
    telefone = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_USUARIO)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = Gerenciador()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
          return self.email

class Formato(models.Model):
    CATEGORIAS_FORMATO = (
        ('EBOOK', 'E-book'),
        ('FISICO', 'Físico'),
    )

    categoria = models.CharField(max_length=20, choices=CATEGORIAS_FORMATO, primary_key=True)

    def __str__(self):
        return self.categoria


class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
    
class CategoriaLivro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Foto (models.Model):
    url = models.CharField(max_length=1000)

class Livro(models.Model):

    nome = models.CharField(max_length=200)
    autorFK = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    ano = models.PositiveIntegerField()
    generoFK = models.ForeignKey('Genero', on_delete=models.CASCADE)
    qtd_paginas = models.PositiveIntegerField()
    formatoFK = models.ForeignKey('Formato', on_delete=models.CASCADE)
    numero_edicao = models.PositiveIntegerField()
    descricao = models.TextField()
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_estoque = models.PositiveIntegerField()
    estrelas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    foto = models.ManyToManyField(Foto)
    categoriaFK = models.ForeignKey('CategoriaLivro', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    STATUS_CHOICES = (
        ('PENDENTE', 'Pendente'),
        ('CONCLUIDO', 'Concluído'),
        ('ATRASADO', 'Atrasado'),
    )

    usuarioFK = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    livroFK = models.ForeignKey('Livro', on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao_prevista = models.DateTimeField()
    data_devolucao_realizada = models.DateTimeField(null=True, blank=True)
    valor_total_emprestimo = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')

    def __str__(self):
        return f"{self.usuarioFK.nome} - {self.livroFK.nome}"

    def save(self, *args, **kwargs):
        if not self.data_devolucao_prevista:
            self.data_devolucao_prevista = self.data_emprestimo + timezone.timedelta(days=7)
        super().save(*args, **kwargs)


class itemEmprestimo(models.Model):
    livroFK = models.ForeignKey('Livro', on_delete=models.CASCADE)
    emprestimoFK = models.ForeignKey('Emprestimo', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.livroFK} - {self.emprestimoFK}"