from tkinter.filedialog import askopenfilename
import yadisk


my_disk = yadisk.YaDisk(token='...')
print(f'Токен подтвержден? {my_disk.check_token()}')


def upload_file(file):
    new_name = input('Введите имя под которым надо сохранить файл в Яндекс Диске: ')
    my_disk.upload(file, new_name)
    print('Загрузка завершена!')


input_file = askopenfilename()
upload_file(input_file)