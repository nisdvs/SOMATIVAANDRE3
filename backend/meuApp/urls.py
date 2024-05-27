from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'usuario',UsuarioView)
router.register(r'formato',FormatoView)
router.register(r'genero',GeneroView)
router.register(r'categoria-livro',CategoriaLivroView)
router.register(r'livro',LivroView)
router.register(r'emprestimo', EmprestimoView)


urlpatterns = router.urls

