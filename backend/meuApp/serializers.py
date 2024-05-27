from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','nome','telefone','categoria','groups']
        many = True
        
class FormatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formato
        fields ='__all__'
        many = True


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'
        many = True


class CategoriaLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaLivro
        fields = '__all__'
        many = True

class FotoSerializer(serializers.ModelSerializer):
    url = serializers.CharField() 
    class Meta:
        model = Foto
        fields = ['url'] 
        
class LivroSerializer(serializers.ModelSerializer):
    foto = FotoSerializer(many=True)
    generoFK = GeneroSerializer (read_only = True)
    formatoFK = FormatoSerializer (read_only = True)
    categoriaFK = CategoriaLivroSerializer (read_only = True)
    class Meta:
        model = Livro
        fields = '__all__'
        many = True

class EmprestimoSerializer(serializers.ModelSerializer):
    usuarioFK = UsuarioSerializer(read_only = True)
    class Meta:
        model: Emprestimo
        fiels = ['data_emprestimo', 'data_devolucao_prevista', ' data_devolucao_realizada', 'valor_total_emprestimo', 'status']
        many = True 

        
class itemEmprestimoSerializer(serializers.ModelSerializer):
    livroFK = LivroSerializer(read_only = True)
    emprestimoFK = EmprestimoSerializer(read_only = True)
    class Meta:
        model: itemEmprestimo
        fiels = ['livroFK', 'emprestimoFK']
        many = True
