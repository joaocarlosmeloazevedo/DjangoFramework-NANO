from django.db import models
from autores.models import Autor

class Livro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) #FK -> Vínculo | on_delete...
    # exclui autor e livro ou vice-versa em modo cascada. Influencia o vinculo das tabelas.
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    paginas = models.IntegerField()
    editora = models.CharField(max_length=50)
    edicao = models.IntegerField()
    ano_publicacao = models.IntegerField()
    idioma = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo