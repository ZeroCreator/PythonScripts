import os
from fid import get_result

PATH = '/home/zerocreator/PythonScripts/fids/Downloads'

def main():
    fids_files_names = os.listdir(PATH)
    for name in fids_files_names:
        get_result(f'{PATH}/{name}')

if __name__ == '__main__':
    main()