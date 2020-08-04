# Generated by Django 3.0.8 on 2020-08-03 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=200)),
                ('default_account', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Account')),
            ],
        ),
    ]
