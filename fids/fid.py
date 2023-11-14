from bs4 import BeautifulSoup

def get_result(file):
    xml_report_part = open(file, 'r')
    soup = BeautifulSoup(xml_report_part, 'xml')
    list_id = soup.select('offer')
    code_list = []
    url_list = []
    print(file)
    print(len(list_id))
    for id in list_id:
        code = id.attrs['id']
        code_list.append(code)
        url = id.url
        url_list.append(url)
        # name = id.select_one('name').text.split(' ')[0]
        name = id.select_one('name').text
        # print(code, name)
        available = id.attrs['available']
        if available == 'true':
            continue
        else:
            print(code, available)


    # print(len(code_list))
    # print(len(set(code_list)))
    # print(len(code_list) == len(set(code_list)))
    # print(len(url_list))
    # print(len(set(url_list)))
    # print(len(url_list) == len(set(url_list)))
    # print(list_id)
    # return summ_result(list_id)
