import requests
from pprint import pprint
import base64
import yadisk

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    def upload_href(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        href = data.get('href')
        return href

    def upload_file_to_disk(self, disk_file_path, file_list):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        need_href = self.upload_href(disk_file_path)
        for filename in file_list:
            response = requests.put(need_href, data=open(filename, 'rb'))
            if response.status_code == 201:
                print('Success')


if __name__ == '__main__':
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    token = 'y0_AgAAAAAXx97qAADLWwAAAADgH--KGSdWObIcTimzTI9XGF2ORU5emqo'
    uploader = YaUploader(token)
    n = 1
    while n < 4:
        uploader.upload_file_to_disk(f'Загрузки/file{n}', file_list)
        n += 1