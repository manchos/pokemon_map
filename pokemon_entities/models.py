from django.db import models


# your models here


class Pokemon(models.Model):
    """Покемон"""
    title_ru = models.CharField(
        max_length=200, default='', blank=True, verbose_name='Имя по-русски')
    title_en = models.CharField(
        max_length=200, default='', blank=True, verbose_name='Имя по-аглицки')
    title_jp = models.CharField(
        max_length=200, default='', blank=True, verbose_name='Имя по-японски')
    description = models.TextField(
       default='', blank=True, verbose_name='Описание')
    photo = models.ImageField(
        upload_to='pokemons', null=True, verbose_name='Изображение')
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Из кого эволюционирует',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='next_evolutions'
    )


    def __str__(self):
        return f"{self.title_ru}"


class PokemonEntity(models.Model):
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    pokemon = models.ForeignKey(
        Pokemon, related_name='pokemon_entities', on_delete=models.CASCADE
    )
    appeared_at = models.DateTimeField(
        default=None, blank=True, verbose_name='Появился в')
    disappeared_at = models.DateTimeField(
        default=None, blank=True, verbose_name='Исчез в')
    level = models.IntegerField(
        default=None, null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(
        default=None, null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(
        default=None, null=True, blank=True, verbose_name='Атака')
    defence = models.IntegerField(
        default=None, null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(
        default=None, null=True, blank=True, verbose_name='Выносливость')


