from django.db import models

# your models here


class Pokemon(models.Model):
    """Покемон"""
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokemons', null=True)

    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    lat = models.FloatField(blank=True)
    lon = models.FloatField(blank=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
