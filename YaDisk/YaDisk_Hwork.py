import requests


file_name = "NewFile.txt"
file_path = 'C:\\Test\\' + file_name
my_token = '....'


class YaUploader:

    # Инициализация класса

    def __init__(self, path: str, token):
        self.target_path = "/" + file_name
        self.file_path = path
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.params_for_get = {'path': self.target_path, 'overwrite': True}
        self.params_for_put = {'path': self.file_path}
        self.headers = {'Authorization': 'OAuth ' + self.token}

# Функция для получения URL для загрузки файла на Я.Диск

    def get_load_url(self):
        get_link = requests.get(url=self.url,
                                params=self.params_for_get,
                                headers=self.headers)

        if get_link.status_code == 200:
            link = get_link.json()
            return link
        else:
            print(f'Ошибка {get_link.status_code}')

# Функция загрузки файла на диск

    def upload(self):
        upload_link = self.get_load_url()
        use_link = requests.put(url=upload_link['href'],
                                params=self.params_for_put,
                                headers=self.headers)
        if use_link.status_code == 201:
            print('Файл успешно загружен!')
        else:
            print('Ошибка загрузки')
        pass


if __name__ == '__main__':
    uploader = YaUploader(file_path, my_token)
    result = uploader.upload()