from django.db import models


# used for img_url by pokemon_entities.exposed_request.RequestExposerMiddleware
exposed_request = ''


class PokemonElementType(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='Стихии')
    img = models.ImageField(
        upload_to='element_types', null=True, blank=True, verbose_name='Изображение')
    weakers = models.ManyToManyField(
        "self", verbose_name='Силен против', related_name='strongers', symmetrical=False,
    )

    @property
    def img_url(self):
        return exposed_request.build_absolute_uri(self.img.url)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стихия'
        verbose_name_plural = 'Стихии'


class Pokemon(models.Model):
    """Покемон"""
    title_ru = models.CharField(
        max_length=200, verbose_name='Имя по-русски')
    title_en = models.CharField(
        max_length=200, default='', blank=True, verbose_name='Имя по-аглицки')
    title_jp = models.CharField(
        max_length=200, default='', blank=True, verbose_name='Имя по-японски')
    description = models.TextField(
       default='', blank=True, verbose_name='Описание')
    photo = models.ImageField(
        upload_to='pokemons', verbose_name='Изображение')
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Из кого эволюционирует',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='next_evolutions'
    )
    element_type = models.ManyToManyField(
        PokemonElementType, related_name='pokemons')

    @property
    def img_url(self):
        return exposed_request.build_absolute_uri(self.photo.url)

    @property
    def pokemon_id(self):
        return self.id

    def __str__(self):
        return f"{self.title_ru}"


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(
        Pokemon, related_name='pokemon_entities', on_delete=models.CASCADE
    )
    appeared_at = models.DateTimeField(verbose_name='Появился в')
    disappeared_at = models.DateTimeField(verbose_name='Исчез в')
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


