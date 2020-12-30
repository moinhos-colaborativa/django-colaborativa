# Generated by Django 2.2.15 on 2020-12-30 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("colaborativa", "0006_remove_extrainfo_profession"),
    ]

    operations = [
        migrations.AddField(
            model_name="extrainfo",
            name="state1",
            field=models.CharField(
                choices=[
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
                ],
                default="RS",
                max_length=2,
                verbose_name="Estado",
            ),
            preserve_default=False,
        ),
    ]
