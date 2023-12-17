# Анна Горшенкова, 11-я когорта — Финальный проект. Инженер по тестированию плюс

import stand_request
import data
def test_find_order_by_track():
    create_response = stand_request.create_order(data.order_body)
    tracking_code = create_response.json()
    track = tracking_code['track']
    final_response = stand_request.get_info_by_track(track)
    assert final_response.status_code == 200