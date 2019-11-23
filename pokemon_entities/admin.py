from django.contrib import admin

from .models import Pokemon, PokemonEntity

class PokemonEntityInline(admin.TabularInline):
    model = PokemonEntity

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    inlines = [PokemonEntityInline]


@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    fields = ('pokemon', 'lat', 'lon', 'appeared_at', 'disappeared_at')







