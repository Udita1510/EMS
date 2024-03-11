# Generated by Django 5.0.2 on 2024-03-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
