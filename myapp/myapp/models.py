from django.db import models

# Create your models here.
'''from django.db import models


class Alunos(models.Model):
    id_aluno = integer_field(
        primary_key=True,
        default=0,

    )    
    nome = models.CharField(
    max_length=255,
    null=False,
    blank=False
    )
    sobrenome = models.CharField(
    max_length=255,
    null=False,
    blank=False
    )
    cpf = models.CharField(
    max_length=14,
    null=False,
    blank=False
    )
    tempo_de_servico = models.IntegerField(
    default=0,
    null=False,
    blank=False
    )
    remuneracao = models.DecimalField(
    max_digits=8,
    decimal_places=2,
    null=False,
    blank=False
    )
    objetos = models.Manager()
'''

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alunos(models.Model):
    id_aluno = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    rg = models.CharField(max_length=8, blank=True, null=True)
    matricula = models.CharField(max_length=8, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'Alunos'
        verbose_name_plural = "alunos"


class Atividadealuno(models.Model):
    id = models.ForeignKey('Atividades', models.DO_NOTHING, db_column='id', blank=True, null=True)
    id_atividade = models.IntegerField(primary_key=True)
    id_aluno = models.IntegerField(blank=True, null=True)
    nota = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'AtividadeAluno'
        verbose_name_plural = "atividadealuno"


class Atividades(models.Model):
    id_atividade = models.OneToOneField('Planoaula', models.DO_NOTHING, db_column='id_atividade', primary_key=True)
    atividade = models.BinaryField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    data_postagem = models.DateField(blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)
    id_disciplina = models.IntegerField(blank=True, null=True)
    id_plano_aula = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Atividades'
        verbose_name_plural = "atividades"


class Disciplinaaluno(models.Model):
    id_matricula = models.OneToOneField('Disciplinas', models.DO_NOTHING, db_column='id_matricula', primary_key=True)
    id_aluno = models.IntegerField(blank=True, null=True)
    id_disciplina = models.IntegerField(blank=True, null=True)
    nota = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'DisciplinaAluno'
        verbose_name_plural = "disciplinaaluno"


class Disciplinas(models.Model):
    id_disciplina = models.OneToOneField('Professores', models.DO_NOTHING, db_column='id_disciplina', primary_key=True)
    id_professor = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=7, blank=True, null=True)
    carga_horaria = models.IntegerField(blank=True, null=True)
    ementa = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'Disciplinas'
        verbose_name_plural = "disciplinas"


class Frequencia(models.Model):
    id_frequencia = models.OneToOneField(Disciplinas, models.DO_NOTHING, db_column='id_frequencia', primary_key=True)
    id_materia = models.IntegerField(blank=True, null=True)
    dia = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'Frequencia'
        verbose_name_plural = "frequencia"


class Frequenciaaluno(models.Model):
    id = models.ForeignKey(Frequencia, models.DO_NOTHING, db_column='id', blank=True, null=True)
    id_aluno = models.IntegerField(primary_key=True)
    id_frequencia = models.IntegerField(blank=True, null=True)
    presenca = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'FrequenciaAluno'
        verbose_name_plural = "frequenciaaluno"


class Planoaula(models.Model):
    id_plano_aula = models.OneToOneField(Disciplinas, models.DO_NOTHING, db_column='id_plano_aula', primary_key=True)
    id_disciplina = models.IntegerField(blank=True, null=True)
    tema_aula = models.CharField(max_length=255, blank=True, null=True)
    conteudo = models.BinaryField(blank=True, null=True)
    metodo = models.CharField(max_length=50, blank=True, null=True)
    dia = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'PlanoAula'
        verbose_name_plural = "planoaula"


class Professores(models.Model):
    id_professor = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    rg = models.CharField(max_length=8, blank=True, null=True)
    codigo = models.CharField(max_length=8, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'Professores'
        verbose_name_plural = "professores"
