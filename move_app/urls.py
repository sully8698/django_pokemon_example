from django.urls import path
from .views import AllMoves, FireMoves, PsychicMoves, SelectedMove

urlpatterns = [
    path('', AllMoves.as_view(), name='all_moves'),
    path('fire/', FireMoves.as_view(), name='fire_moves'),
    path('psychic/', PsychicMoves.as_view(), name='psychic_moves'),
    path('<str:name>/', SelectedMove.as_view(), name='selected_move')
]