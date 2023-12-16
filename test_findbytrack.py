import stand_request

def test_find_order_by_track():
    we_got_info_response = stand_request.get_info_by_track()
    assert we_got_info_response.status_code == 200