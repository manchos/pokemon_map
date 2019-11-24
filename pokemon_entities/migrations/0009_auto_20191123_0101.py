# Generated by Django 2.2.3 on 2019-11-22 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20191122_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.Pokemon', verbose_name='Из кого эволюционирует'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=None, verbose_name='Появился в'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default=None, verbose_name='Исчез в'),
        ),
    ]
