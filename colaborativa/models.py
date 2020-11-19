from django.conf import settings
from django.db import models

USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class ExtraInfo(models.Model):
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, null=True)
    GENDER_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )
    HOSPITAL_CHOICES = (
        ("HCor Hospital do Coração", "HCor Hospital do Coração"),
        ("Hospital Alemão Oswaldo Cruz", "Hospital Alemão Oswaldo Cruz"),
        ("Hospital Israelita Albert Einstein", "Hospital Israelita Albert Einstein"),
        ("Hospital Moinhos de Vento", "Hospital Moinhos de Vento"),
        ("Hospital Sírio Libanês", "Hospital Sírio Libanês"),
    )
    cpf = models.CharField(verbose_name="CPF", blank=True, null=True, max_length=15)
    gender = models.CharField(verbose_name="Gênero", blank=True, null=True, max_length=1, choices=GENDER_CHOICES)
    profession = models.CharField(verbose_name="Profissão", blank=True, null=True, max_length=100)
    occupation_area = models.CharField(verbose_name="Área de atuação", blank=True, null=True, max_length=100)
    hospital_work = models.CharField(verbose_name="Hospital onde trabalha", blank=True, null=True, max_length=100)
    city = models.CharField(verbose_name="Cidade", blank=True, null=True, max_length=100)
    state = models.CharField(verbose_name="Estado", blank=True, null=True, max_length=100)
    health_hands = models.BooleanField(verbose_name="Participa ou participou do 'Saúde em Nossas Mãos'", default=False)
    health_hands_where = models.CharField(
        verbose_name="(Se sim na l) Hospital que orientou seu projeto:",
        blank=True,
        null=True,
        max_length=100,
        choices=HOSPITAL_CHOICES,
    )
