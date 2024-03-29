# Generated by Django 3.2.20 on 2023-09-05 12:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('recipemanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=200)),
                ('password', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('passcode', models.CharField(max_length=4)),
                ('account_type', models.CharField(max_length=100)),
                ('bank_account_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipemanager.user')),
            ],
        ),
    ]
