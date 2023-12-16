import configuration
import requests
import data

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

response = create_order(data.order_body)
tracking_code = response.json()
track = tracking_code['track']

def get_info_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={"t":track})



