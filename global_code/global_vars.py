from datetime import datetime


def get_current_details():
    longitude = '93.2358'
    latitude = '44.9805'
    time = datetime.now()
    data = {'longitude': longitude, 'latitude': latitude, 'current_time': time}
    return data