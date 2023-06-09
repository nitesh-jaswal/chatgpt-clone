# Generated by Django 4.2.1 on 2023-05-28 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("question_text", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("answer_text", models.CharField(max_length=500)),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=4, max_digits=8, verbose_name="amount charged"
                    ),
                ),
                ("tokens", models.IntegerField(verbose_name="tokens generated")),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="simplechat.question",
                    ),
                ),
            ],
        ),
    ]
