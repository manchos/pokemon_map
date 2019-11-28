from django.contrib import admin

from .models import Pokemon, PokemonEntity, PokemonElementType


class PokemonEntityInline(admin.TabularInline):
    model = PokemonEntity


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    inlines = [PokemonEntityInline]


@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    pass


@admin.register(PokemonElementType)
class PokemonElementTypeAdmin(admin.ModelAdmin):
    pass





