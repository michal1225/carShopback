# Generated by Django 4.2 on 2023-05-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Part",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("img", models.ImageField(blank=True, upload_to="")),
                ("price", models.DecimalField(decimal_places=2, max_digits=40)),
            ],
            options={
                "ordering": ["created"],
            },
        ),
    ]
