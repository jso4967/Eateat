# Generated by Django 2.1.5 on 2019-02-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='meal_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='meal',
            name='price_range',
            field=models.CharField(choices=[('높음', '높음'), ('중간', '중간'), ('낮음', '낮음')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='meal',
            name='satisfaction',
            field=models.CharField(choices=[('높음', '높음'), ('중간', '중간'), ('낮음', '낮음')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='meal',
            name='restaurant_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
