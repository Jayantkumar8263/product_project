# Generated by Django 5.0.6 on 2024-06-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_noumber', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
