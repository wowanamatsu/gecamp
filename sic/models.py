from django.db import models
from django.utils import timezone


#===============================================================================================
class Pais(models.Model):

    nome = models.CharField(max_length=30, unique=True)
    codigo = models.CharField(max_length=5, unique=True, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        db_table = 'paises'


#===============================================================================================
class Estado(models.Model):

    nome = models.CharField(max_length=30, unique=True)
    pais_id = models.ForeignKey('Pais', on_delete=models.CASCADE)
    sigla = models.CharField(max_length=5, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'estados'


#===============================================================================================
class Municipio(models.Model):

    nome = models.CharField(max_length=30)
    estado_id = models.ForeignKey('Estado', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        db_table = 'municipios'


#===============================================================================================
class Cidade(models.Model):

    nome = models.CharField(max_length=30)
    municipio_id = models.ForeignKey('Municipio', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        db_table = 'cidades'


#===============================================================================================
class Bairro(models.Model):

    nome = models.CharField(max_length=30)
    cidade_id = models.ForeignKey('Cidade', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'
        db_table = 'bairros'


#===============================================================================================
class Escolaridade(models.Model):
    nivel_escolar = models.CharField(max_length=30)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nivel_escolar

    class Meta:
        verbose_name = 'Escolaridade'
        verbose_name_plural = 'Escolaridades'
        db_table = 'escolaridades'


#===============================================================================================
class Profissao(models.Model):
    nome = models.CharField(max_length=30)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Profissao'
        verbose_name_plural = 'Profissões'
        db_table = 'profissoes'

#===============================================================================================
class Pessoa(models.Model):
    UF = []
    M_UF = []

    # Dados básicos
    indicado_por = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=80)
    nome_social = models.CharField(max_length=80, blank=True, null=True)
    data_nascimento = models.DateField('Data Nasc.', blank=True, null=True)
    sexo = models.CharField(
        choices=(
            ('Masculino', 'Masculino'),
            ('Feminino', 'Feminino'),
        ), max_length=10
    )
    nome_da_mae = models.CharField('Nome da mãe', max_length=80, blank=True, null=True)
    nome_do_pai = models.CharField('Nome do pai', max_length=80, blank=True, null=True)
    naturalidade = models.CharField(max_length=100, blank=True, null=True)

    # Formas de contato
    endereco = models.CharField('Endereço', max_length=50)
    cep = models.CharField('CEP', max_length=14, blank=True, null=True)
    email = models.CharField(max_length=80, unique=True, blank=True, null=True)
    telefone_celular = models.CharField('Telefone Celular', max_length=14, blank=True, null=True)
    telefone_residencial = models.CharField('Telenone Residencial', max_length=14, blank=True, null=True)
    telefone_trabalho = models.CharField('Telefone do Trabalho', max_length=14, blank=True, null=True)
    

    
    # Documentos
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    rg = models.CharField('RG', max_length=10, blank=True, null=True)
    rg_uf = models.IntegerField('RG / UF', choices=UF, blank=True, null=True)
    titulo_eleitor = models.CharField('Título', max_length=20, blank=True, null=True)
    titulo_secao = models.CharField('Seção', max_length=6, blank=True, null=True)
    titulo_zona = models.CharField('Zona', max_length=6, blank=True, null=True)
    titulo_uf = models.IntegerField('Título / Município', choices=M_UF, blank=True, null=True)

    
    
    estado_civil = models.CharField('Estado civil',
                                    choices=(
                                        ('Casado(a)', 'Casado(a)'),
                                        ('Solteiro(a)', 'Solteiro(a)'),
                                        ('Outros', 'Outros'),
                                    ), max_length=12, default='Solteiro'
                                    )
    
    
    escolaridade_id = models.ForeignKey('Escolaridade', null=True, blank=True, on_delete=models.CASCADE)
    profissao = models.ForeignKey('Profissao', null=True, blank=True, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)
    

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoas'

