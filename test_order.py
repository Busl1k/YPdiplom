import pytest
from stand import create_order, get_order_by_track

def test_get_order_by_track():
    """Тест: создаём заказ и проверяем, что его можно найти по треку"""
    
    track = create_order()
    assert track is not None, "Ошибка: трек заказа не получен"

    response = get_order_by_track(track)
    assert response.status_code == 200, "Ошибка: заказ по треку не найден"

    order_data = response.json()
    assert "order" in order_data, "Ошибка: в ответе нет ключа 'order'"
    assert order_data["order"]["track"] == track, "Ошибка: трек заказа не совпадает"
