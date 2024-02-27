# Generated by Django 4.2.10 on 2024-02-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(db_index=True, max_length=45, verbose_name='name')),
                ('password', models.CharField(db_index=True, max_length=150, verbose_name='password')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='email')),
                ('token', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='token')),
                ('token_expired', models.DateTimeField(blank=True, null=True, verbose_name='token_expired')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]