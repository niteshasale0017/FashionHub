# Generated by Django 3.0.8 on 2020-12-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('pant_type', models.CharField(choices=[('FORMAL', 'formal'), ('CASUAL', 'casual'), ('JEANS', 'jeans')], max_length=10)),
                ('size_28', models.IntegerField()),
                ('size_30', models.IntegerField()),
                ('size_32', models.IntegerField()),
                ('size_34', models.IntegerField()),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('pant_image', models.ImageField(upload_to='pant_photo')),
                ('status', models.CharField(choices=[('REGULAR', 'regular'), ('TREND', 'trend'), ('TODAYS DEAL', 'todays deal')], max_length=12)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('shirt_type', models.CharField(choices=[('FORMAL', 'formal'), ('CASUAL', 'casual'), ('HOODIE', 'hoodie')], max_length=10)),
                ('size_m', models.IntegerField()),
                ('size_l', models.IntegerField()),
                ('size_xl', models.IntegerField()),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('shirt_image', models.ImageField(upload_to='shirt_photo')),
                ('status', models.CharField(choices=[('REGULAR', 'regular'), ('TREND', 'trend'), ('TODAYS DEAL', 'todays deal')], max_length=12)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('shoe_type', models.CharField(choices=[('FORMAL', 'formal'), ('CANVAS', 'canvas'), ('LOFER', 'lofer'), ('SNEAKERS', 'sneakers')], max_length=10)),
                ('size_7', models.IntegerField()),
                ('size_8', models.IntegerField()),
                ('size_9', models.IntegerField()),
                ('size_10', models.IntegerField()),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('shoe_image', models.ImageField(upload_to='shoe_photo')),
                ('status', models.CharField(choices=[('REGULAR', 'regular'), ('TREND', 'trend'), ('TODAYS DEAL', 'todays deal')], max_length=12)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
    ]
