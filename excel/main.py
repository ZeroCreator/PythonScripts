import os
from script import get_result
from format_date_time import format_date_time

# Путь до папки с файлами
PATH = '/home/zerocreator/ExcelProject/excel/Downloads'

# Применяем функцию к каждому файлу из папки
def main():
    excel_files_names = os.listdir(PATH)
    for name in excel_files_names:
        # get_result(f'{PATH}/{name}')
        format_date_time(f'{PATH}/{name}')


if __name__ == '__main__':
    main()
