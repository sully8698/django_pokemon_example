from django.urls import path, register_converter
from .views import AllPokemon, SelectedPokemon
from .converters import IntOrStrConverter


register_converter(IntOrStrConverter, 'int_or_str')

urlpatterns = [
    path('', AllPokemon.as_view(), name='all_pokemon'), # if I access "localhost:8000/api/v1/pokemon/" (and I don't add anything after), then return all the pokemon in JSON format.
    path('<int_or_str:id>', SelectedPokemon.as_view(), name='selected_pokemon')
]