from django.contrib import admin

# Register your models here.

from myapp.models import Alunos, Atividadealuno, Atividades, Disciplinaaluno, Disciplinas, Frequencia, Frequenciaaluno, Planoaula, Professores

#admin.site.register(Alunos)
admin.site.register(Atividadealuno)
admin.site.register(Atividades)
admin.site.register(Disciplinaaluno)
admin.site.register(Disciplinas)
admin.site.register(Frequencia)
admin.site.register(Frequenciaaluno)
admin.site.register(Planoaula)
admin.site.register(Professores)


class AlunosAdmin(admin.ModelAdmin):
    search_fields = ['nome']

admin.site.register(Alunos, AlunosAdmin)