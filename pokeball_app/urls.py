#pokeball_app/urls.py
from django.urls import path, register_converter
from .converters import BallTypeConverter
from .views import PokeballImg

# register the converter we created so we could utilize it in our paths
register_converter(BallTypeConverter, 'pokeball')

urlpatterns = [
    # utilize the registered converter to ensure the parameter is valid
    path("<pokeball:ball>/", PokeballImg.as_view(), name='pokeball'),
]