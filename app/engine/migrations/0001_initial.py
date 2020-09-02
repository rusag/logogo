# Generated by Django 3.0.7 on 2020-08-02 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Font',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('font', models.FileField(upload_to='fonts')),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
    ]
