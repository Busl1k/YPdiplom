import requests
from configuration import URL_SERVICE, ORDERS_URL, TRACK_URL
from data import ORDER_DATA

def create_order():
    """Создаёт заказ и возвращает его трек"""
    response = requests.post(f"{URL_SERVICE}{ORDERS_URL}", json=ORDER_DATA)
    
    if response.status_code == 201:
        return response.json().get("track")
    else:
        return None

def get_order_by_track(track):
    """Получает заказ по номеру трека"""
    response = requests.get(f"{URL_SERVICE}{TRACK_URL}{track}")
    return response
