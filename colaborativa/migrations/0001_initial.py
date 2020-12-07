# Generated by Django 2.2.15 on 2020-12-07 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ExtraInfo",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("cpf", models.CharField(max_length=15, verbose_name="CPF")),
                ("profession", models.CharField(max_length=100, verbose_name="Profissão")),
                ("occupation_area", models.CharField(max_length=100, verbose_name="Área de atuação")),
                ("hospital_work", models.CharField(max_length=100, verbose_name="Hospital onde trabalha")),
                (
                    "health_hands",
                    models.BooleanField(
                        default=False, verbose_name="Participa ou participou do 'Saúde em Nossas Mãos'"
                    ),
                ),
                (
                    "health_hands_where",
                    models.CharField(
                        choices=[
                            ("HCor Hospital do Coração", "HCor Hospital do Coração"),
                            ("Hospital Alemão Oswaldo Cruz", "Hospital Alemão Oswaldo Cruz"),
                            ("Hospital Israelita Albert Einstein", "Hospital Israelita Albert Einstein"),
                            ("Hospital Moinhos de Vento", "Hospital Moinhos de Vento"),
                            ("Hospital Sírio Libanês", "Hospital Sírio Libanês"),
                        ],
                        max_length=100,
                        verbose_name="(Se sim na l) Hospital que orientou seu projeto:",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
