# Generated by Django 3.2.10 on 2021-12-15 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cookie_stands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('hourly_sales', models.JSONField(blank=True, default=list)),
                ('minimum_customers_per_hour', models.IntegerField(default=0)),
                ('maximum_customers_per_hour', models.IntegerField(default=0)),
                ('average_cookies_per_sale', models.FloatField(default=0)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
