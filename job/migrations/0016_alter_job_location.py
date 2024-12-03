# Generated by Django 4.2.6 on 2024-12-02 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0015_alter_job_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="job.location"
            ),
        ),
    ]