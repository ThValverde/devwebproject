# Generated by Django 5.2.2 on 2025-06-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_medicamento_dosagem_valor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='dosagem_valor',
            field=models.DecimalField(blank=True, decimal_places=0, help_text="Ex: 50mg/g, adicionar 500 aqui e selecionar 'mg/g' abaixo.", max_digits=10, null=True, verbose_name='Valor da Dosagem'),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='quantidade_por_embalagem',
            field=models.DecimalField(blank=True, decimal_places=0, help_text='Nº de comprimidos/cápsulas por caixa ou volume total em ml. Ex: 20 comprimidos ou 500 ml.', max_digits=10, null=True, verbose_name='Quantidade por Embalagem'),
        ),
    ]
