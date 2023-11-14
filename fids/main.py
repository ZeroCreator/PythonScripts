import os
from bs4 import BeautifulSoup
from fid import get_result

# Путь до папки с файлами
PATH = '/home/zerocreator/PythonScripts/fids/Downloads'

# Применяем функцию к каждому файлу из папки
def main():
    # code_list = []
    # url_list = []
    # code_set = ()
    # url_set = ()
    fids_files_names = os.listdir(PATH)
    for name in fids_files_names:
        # res_code_set = ()
        # res_code_list = []
        get_result(f'{PATH}/{name}')
    # file1 = (f'{PATH}/index2.html')
    # xml_report_part = open(file1, 'r')
    # soup = BeautifulSoup(xml_report_part, 'xml')
    # list_id = soup.select('offer')
    # for id in list_id:
    #     code = id.attrs['id']
    #     code_list.append(code)
    #     code_set = code_set + (code,)
    #     url = id.url
    #     url_list.append(url)
    #     url_set = url_set + (url,)
    #     # name = id.select_one('name').text.split(' ')[0]
    #     # print(name)
    # # res_code_set = res_code_set + get_result.code_set
    # # print(res_code_set)
    # print(len(code_list))
    # print(len(set(code_set)))
    # print(len(code_list) == len(set(code_set)))
    # print(len(url_list))
    # print(len(set(url_set)))
    # print(len(url_list) == len(set(url_set)))
    #
    #
    # file1 = (f'{PATH}/index1.html')
    # xml_report_part = open(file1, 'r')
    # soup = BeautifulSoup(xml_report_part, 'xml')
    # list_id = soup.select('offer')
    # for id in list_id:
    #     code = id.attrs['id']
    #     code_list.append(code)
    #     code_set = code_set + (code,)
    #     url = id.url
    #     url_list.append(url)
    #     url_set = url_set + (url,)
    #
    # print(len(code_list))
    # print(len(set(code_set)))
    # print(len(code_list) == len(code_set))
    # print(len(url_list))
    # print(len(set(url_set)))
    # print(len(url_list) == len(set(url_set)))
    #
    # file1 = (f'{PATH}/index.html')
    # xml_report_part = open(file1, 'r')
    # soup = BeautifulSoup(xml_report_part, 'xml')
    # list_id = soup.select('offer')
    # for id in list_id:
    #     code = id.attrs['id']
    #     code_list.append(code)
    #     code_set = code_set + (code,)
    #     url = id.url
    #     url_list.append(url)
    #     url_set = url_set + (url,)
    #
    # print(len(code_list))
    # print(len(set(code_set)))
    # print(len(code_list) == len(code_set))
    # print(len(url_list))
    # print(len(set(url_set)))
    # print(len(url_list) == len(set(url_set)))

if __name__ == '__main__':
    main()
