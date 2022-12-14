# Generated by Django 2.1.5 on 2022-09-30 20:53

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('initial_deposit', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            managers=[
                ('Accounts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawl', 'Withdrawl')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.CharField(max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkbook.Account')),
            ],
            managers=[
                ('Transactions', django.db.models.manager.Manager()),
            ],
        ),
    ]
