# Generated by Django 3.2.9 on 2021-12-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listcat', '0003_listcats_temperament'),
    ]

    operations = [
        migrations.AddField(
            model_name='listcats',
            name='body_type',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listcats',
            name='coat',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listcats',
            name='coat_color',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listcats',
            name='lifespan',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listcats',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]