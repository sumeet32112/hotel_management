# Generated by Django 3.2.8 on 2021-11-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_auto_20211116_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hotel',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotelName',
            field=models.TextField(max_length=200),
        ),
    ]
