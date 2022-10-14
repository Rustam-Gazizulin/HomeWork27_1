# Generated by Django 4.1.1 on 2022-10-12 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_location_lat_alter_location_lng_and_more'),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='users.user', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ads', to='ads.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(null=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=60, unique=True, verbose_name='Категория'),
        ),
    ]