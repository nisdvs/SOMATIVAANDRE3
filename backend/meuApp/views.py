from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class CustomModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class UsuarioView(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = Usuario.objects.filter(id=user.id)        
        return queryset
    
class FormatoView(ModelViewSet):
    queryset = Formato.objects.all() 
    serializer_class = FormatoSerializer
    
    
class GeneroView(ModelViewSet):
    queryset = Genero.objects.all() 
    serializer_class = GeneroSerializer
    
    
class CategoriaLivroView(ModelViewSet):
    queryset = CategoriaLivro.objects.all() 
    serializer_class = CategoriaLivroSerializer


class LivroView(ModelViewSet):
    queryset = Livro.objects.all() 
    serializer_class = LivroSerializer
    
    
class EmprestimoView(ModelViewSet):
    queryset = Emprestimo.objects.all() 
    serializer_class = EmprestimoSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user = request.user
        
        # Verifique se o usuário tem devoluções atrasadas
        atrasados = Emprestimo.objects.filter(
            usuario=user, data_devolucao__isnull=True, data_prevista_devolucao__lt=timezone.now()
        )
        if atrasados.exists():
            return Response({"error": "Você não pode realizar novos empréstimos enquanto tiver devoluções atrasadas."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verifique se o usuário já tem 3 livros emprestados simultaneamente
        livros_emprestados = itemEmprestimo.objects.filter(
            emprestimo__usuario=user, emprestimo__data_devolucao__isnull=True
        ).count()
        if livros_emprestados + len(request.data.get('livros', [])) > 3:
            return Response({"error": "Você já atingiu o limite de 3 livros emprestados simultaneamente."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Caso contrário, permita o empréstimo
        return super().create(request, *args, **kwargs)


class itemEmprestimo(ModelViewSet):
    queryset = itemEmprestimo.objects.all()
    serializer_class = itemEmprestimoSerializer
    permission_classes = (IsAuthenticated,)