# Generated by Django 5.1.4 on 2024-12-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='notes', to='notes.tag'),
        ),
    ]
