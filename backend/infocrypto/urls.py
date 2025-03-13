from django.urls import path
from infocrypto import views
#URL config
urlpatterns = [
    path("coin/<str:COIN_ID>/", views.CoinAsk, name="coin_data")
]