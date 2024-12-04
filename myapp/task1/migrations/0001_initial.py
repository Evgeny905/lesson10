# Generated by Django 5.1.3 on 2024-12-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=10, max_digits=1000)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=10, max_digits=1000)),
                ('size', models.DecimalField(decimal_places=10, max_digits=1000)),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(default=False)),
                ('DecimalField', models.DecimalField(decimal_places=10, max_digits=1000)),
                ('BooleanField', models.BooleanField()),
                ('buyer', models.ManyToManyField(related_name='games', to='task1.buyer')),
            ],
        ),
    ]
