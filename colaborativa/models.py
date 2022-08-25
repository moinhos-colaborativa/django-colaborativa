from django.conf import settings
from django.db import models

USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")

STATES_CHOICES = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
)


class ExtraInfo(models.Model):
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, null=True)
    GENDER_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )
    HOSPITAL_CHOICES = (
        ("Não participou", "Não participou"),
        ("HCor Hospital do Coração", "Participou no HCor Hospital do Coração"),
        ("Hospital Alemão Oswaldo Cruz", "Participou no Hospital Alemão Oswaldo Cruz"),
        ("Hospital Israelita Albert Einstein", "Participou no Hospital Israelita Albert Einstein"),
        ("Hospital Moinhos de Vento", "Participou no Hospital Moinhos de Vento"),
        ("Hospital Sírio Libanês", "Participou no Hospital Sírio Libanês"),
        ("Hospital Beneficiência Portuguesa - BP", "Participou no Hospital Beneficiência Portuguesa - BP"),
    )
    cpf = models.CharField(verbose_name="CPF", max_length=14, unique=True)
    # gender_ = models.CharField(verbose_name="Gênero", max_length=1, choices=GENDER_CHOICES)
    # profession = models.CharField(verbose_name="Profissão", max_length=100)
    occupation_area = models.CharField(verbose_name="Área de atuação", max_length=100)
    hospital_work = models.CharField(verbose_name="Hospital onde trabalha", max_length=100)
    # city_ = models.CharField(verbose_name="Cidade", max_length=100)
    # health_hands = models.BooleanField(
    #     verbose_name="Participa ou participou do 'Saúde em Nossas Mãos'", blank=False, null=False
    # )
    health_hands_where = models.CharField(
        verbose_name="Participou do 'Saúde em Nossas Mãos'?", max_length=100, choices=HOSPITAL_CHOICES,
    )
    state1 = models.CharField(verbose_name="Estado", max_length=2, choices=STATES_CHOICES)
