import os
from tqdm import tqdm


class TXTLoader(object):
    def __init__(self, txt_file_path=None):
        self.title_list = []
        self.data_list_list = []

        if txt_file_path is not None:
            self.loadFile(txt_file_path)
        return

    def reset(self):
        self.title_list = []
        self.data_list_list = []
        return True

    def loadFile(self, txt_file_path):
        if not os.path.exists(txt_file_path):
            print('[ERROR][TXTLoader::loadFile]')
            print('\t txt file not exist!')
            print('\t', txt_file_path)

        with open(txt_file_path, 'r', encoding='utf-8') as f:
            data = f.readline()
            print(data)
        return True
