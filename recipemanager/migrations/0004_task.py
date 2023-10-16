# Generated by Django 3.2.20 on 2023-09-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipemanager', '0003_alter_accounts_account_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
