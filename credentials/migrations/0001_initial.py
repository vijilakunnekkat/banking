# Generated by Django 4.1.7 on 2023-06-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=250)),
                ('account', models.CharField(max_length=250)),
                ('materials', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
