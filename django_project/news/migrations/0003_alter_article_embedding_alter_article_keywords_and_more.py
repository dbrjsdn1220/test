# Generated by Django 5.1.2 on 2025-04-25 04:12

import pgvector.django.vector
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_rename_news_article_article"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="embedding",
            field=pgvector.django.vector.VectorField(dimensions=1536),
        ),
        migrations.AlterField(
            model_name="article",
            name="keywords",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="article",
            name="url",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
