# Generated by Django 5.0.3 on 2024-03-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recepts", "0003_alter_recept_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categories",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="recept",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]