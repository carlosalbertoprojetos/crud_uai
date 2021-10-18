# Generated by Django 3.2.8 on 2021-10-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Nome/Razão Social')),
                ('cpf_cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CPF/CNPJ')),
                ('celular', models.IntegerField(null=True, verbose_name='Celular')),
                ('cep', models.CharField(max_length=8, verbose_name='Cep')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereco')),
                ('numero', models.CharField(max_length=8, verbose_name='Número')),
                ('cidade', models.CharField(max_length=255, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=255, verbose_name='Estado')),
                ('situacao', models.CharField(choices=[('2', 'Reprovado'), ('1', 'Aprovado'), ('0', 'Pendente')], default='Pendente', max_length=13, verbose_name='Situação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Usuário ativo')),
                ('equipe', models.BooleanField(default=False, verbose_name='Membro da equipe')),
                ('admin', models.BooleanField(default=True, verbose_name='Admin')),
                ('criadoem', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizadoem', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
    ]
