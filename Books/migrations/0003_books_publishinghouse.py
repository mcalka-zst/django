# Generated by Django 4.0.1 on 2022-01-29 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_publishinghouse_alter_books_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='publishingHouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Books.publishinghouse'),
        ),
    ]