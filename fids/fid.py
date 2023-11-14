from bs4 import BeautifulSoup

def get_result(file):
    xml_report_part = open(file, 'r')
    soup = BeautifulSoup(xml_report_part, 'xml')
    list_id = soup.select('offer')
    code_list = []
    url_list = []
    code_set = ()
    url_set = ()
    for id in list_id:
        code = id.attrs['id']
        code_list.append(code)
        code_set = code_set + (code,)
        url = id.url
        url_list.append(url)
        url_set = url_set + (url,)
        # name = id.select_one('name').text.split(' ')[0]
        name = id.select_one('name').text
        print(code, name)


    # print(len(code_list))
    # print(len(code_set))
    # print(len(code_list) == len(code_set))
    # print(len(url_list))
    # print(len(url_set))
    # print(len(url_list) == len(url_set))
    # return code_list, code_set
    # print(list_id)
    # return summ_result(list_id)


def summ_result(list_id):
    result_list = ''
    result_list = result_list + list_id
    print(len(result_list))
#
#
#     url_summ = code_set + url_set
#     print(print(len(code_list) == len(code_set)))
#     print(len(url_list) == len(url_set))



