# Generated by Django 5.0 on 2024-03-25 05:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_app', '0006_delete_equipments'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField(default=False)),
                ('Hour', models.IntegerField(blank=True, null=True)),
                ('Day', models.IntegerField(blank=True, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Proof', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment_app.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
