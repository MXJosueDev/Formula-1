# Generated by Django 5.1.3 on 2024-11-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('team_color', models.CharField(max_length=50)),
                ('points', models.IntegerField()),
                ('logo', models.ImageField(upload_to='logos/')),
                ('car', models.ImageField(upload_to='cars/')),
            ],
        ),
    ]
