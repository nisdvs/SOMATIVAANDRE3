# Generated by Django 4.2.5 on 2024-05-26 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='livro',
            name='imagem_capa',
        ),
        migrations.AddField(
            model_name='livro',
            name='foto',
            field=models.ManyToManyField(to='meuApp.foto'),
        ),
    ]
