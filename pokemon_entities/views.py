import folium


from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import Pokemon
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, popup, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
        popup=popup,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.prefetch_related('pokemon_entities')
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon in pokemons:
        for pokemon_entity in pokemon.pokemon_entities.all():
            url = '<a href="{}" target="_top">{}</a>'.format(
                request.build_absolute_uri(reverse('pokemon', args=[str(pokemon.id)])),
                    pokemon.title_ru,
                )
            pokemon_url = folium.Html(url, script=True)
            popup = folium.Popup(pokemon_url, max_width=3000)
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon,
                pokemon.title_ru,
                popup,
                pokemon.img_url
            )

    pokemons_on_page = []

    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.img_url,
            'title_ru': pokemon.title_ru,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.prefetch_related('pokemon_entities').get(
            pk=int(pokemon_id)
        )

    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    try:
        pokemon_next_evolution = pokemon.next_evolutions.get()
    except ObjectDoesNotExist:
        pokemon_next_evolution = None

    element_type_list = []
    for element_type in pokemon.element_type.all():
        element_type_list.append({
            'img_url': element_type.img_url,
            'title': element_type.title,
            'strong_against': element_type.weakers.all()
        })

    pokemon_on_page = {
        'pokemon_id': pokemon.id,
        'img_url': pokemon.img_url,
        'title_ru': pokemon.title_ru,
        'description': pokemon.description,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'previous_evolution': pokemon.previous_evolution,
        'next_evolution': pokemon_next_evolution,
        'element_type': element_type_list,
    }

    for pokemon_entity in pokemon.pokemon_entities.all():

        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon.title_ru, pokemon.title_ru, pokemon.img_url
        )

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_on_page})
