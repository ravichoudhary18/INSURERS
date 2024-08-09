# Generated by Django 4.2.5 on 2024-08-09 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('insurance_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=255)),
                ('month', models.CharField(max_length=255)),
                ('clubbed_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_created_by', to=settings.AUTH_USER_MODEL)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.file')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]