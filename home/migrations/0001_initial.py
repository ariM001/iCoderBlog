# Generated by Django 4.0.6 on 2022-08-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75)),
                ('email', models.CharField(max_length=75)),
                ('phone', models.CharField(max_length=12)),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
    ]
