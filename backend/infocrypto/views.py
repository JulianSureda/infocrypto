from django.shortcuts import render
from django.http import JsonResponse
from infocrypto.cc_api import CoinData
# Create your views here.

def CoinAsk(request, COIN_ID):
    data = CoinData(COIN_ID)
    
    # Handle errors if coin not found
    if 'data' not in data:
        return JsonResponse({"error": "Coin not found"}, status=404)
    
    return JsonResponse(data['data'])  # Return JSON data