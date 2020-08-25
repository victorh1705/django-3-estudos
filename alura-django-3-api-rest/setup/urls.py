from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from escola.views import AlunosViewSet, CursosViewSet, ListarMatriculasAluno

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListarMatriculasAluno.as_view()),
]
