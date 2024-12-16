import configparser
import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'

config = configparser.ConfigParser()
config.read("config.ini")
# token = config['YANDEX']['token']
token = ''


def create_folder(folder_name: str) -> bool:
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': folder_name}
    response = requests.put(URL, headers=headers, params=params)
    if response.status_code == 201:
        return True
    else:
        return False
