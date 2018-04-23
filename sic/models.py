from django.db import models

class Pessoa(models.Model):
    UF = []
    M_UF = []

    nome = models.CharField(max_length=80)
    nome_social = models.CharField(max_length=80, blank=True, null=True)
    indicado_por = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    aliado = models.CharField(
        choices=(
            ('sim', 'SIM'),
            ('nao', 'NÃO')
        ), max_length=3, default='nao'
    )
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    rg = models.CharField('RG', max_length=10, blank=True, null=True)
    rg_uf = models.IntegerField('RG / UF', choices=UF, blank=True, null=True)
    titulo = models.CharField('Título', max_length=20, blank=True, null=True)
    titulo_secao = models.CharField('Seção', max_length=6, blank=True, null=True)
    titulo_zona = models.CharField('Zona', max_length=6, blank=True, null=True)
    titulo_uf = models.IntegerField('Título / Município', choices=M_UF, blank=True, null=True)
    data_nascimento = models.DateField('Aniversário')
    sexo = models.CharField(
        choices=(
            ('M', 'Masculino'),
            ('F', 'Feminino'),
        ), max_length=1
    )
    estado_civil = models.CharField('Estado civil',
                                    choices=(
                                        ('Casado', 'Casado(a)'),
                                        ('Solteiro', 'Solteiro(a)'),
                                        ('Outros', 'Outros'),
                                    ), max_length=8, default='Solteiro'
                                    )
    naturalidade = models.CharField(max_length=100, blank=True, null=True)
    escolaridade = models.CharField(
        choices=(
            ('efc', 'Ensino Fundamental Completo'),
            ('efi', 'Ensino Fundamental Incompleto'),
            ('emc', 'Ensino Médio Completo'),
            ('emi', 'Ensino Médio Incompleto'),
            ('ctc', 'Curso Técnico Completo'),
            ('cti', 'Curso Técnico Incompleto'),
            ('nsc', 'Curso Superior Completo'),
            ('nsi', 'Curso Superior Incompleto'),
            ('mes', 'Mestrado'),
            ('dr', 'Doutorado'),
            ('phd', 'Pós-Doutorado'),
        ), max_length=3, blank=True, null=True
    )
    profissao = models.CharField('Profissão', max_length=80, blank=True, null=True)
    nome_da_mae = models.CharField('Nome da Mãe', max_length=80, blank=True, null=True)
    nome_do_pai = models.CharField(max_length=80, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=50)
    cep = models.CharField('CEP', max_length=14, blank=True, null=True)
    email = models.CharField(max_length=80, unique=True, blank=True, null=True)
    telefone_celular = models.CharField('Telefone Celular', max_length=14, blank=True, null=True)
    telefone_residencial = models.CharField('Telenone Residencial', max_length=14, blank=True, null=True)
    telefone_trabalho = models.CharField('Telefone do Trabalho', max_length=14, blank=True, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoas'

