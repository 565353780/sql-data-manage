import os
from sql_data_manager.Module.txt_loader import TXTLoader


class DataMatcher(object):
    def __init__(self, txt_file_path_dict=None, remove_quotes=True):
        self.txt_loader_dict = {}

        if txt_file_path_dict is not None:
            self.loadData(txt_file_path_dict, remove_quotes)
        return

    def reset(self):
        if len(self.txt_loader_dict.keys()) > 0:
            for txt_loader in self.txt_loader_dict.values():
                txt_loader.reset()

        self.txt_loader_dict = {}
        return True

    def loadData(self, txt_file_path_dict, remove_quotes=False):
        if len(txt_file_path_dict.keys()) == 0:
            print('[ERROR][DataMatcher::loadData]')
            print('\t txt file path dict is empty!')
            return False

        for key, txt_file_path in txt_file_path_dict.items():
            if not os.path.exists(txt_file_path):
                print('[WARN][DataMatcher::loadData]')
                print('\t txt file not exist!')
                print('\t', txt_file_path)
                continue

            self.txt_loader_dict[key] = TXTLoader(txt_file_path, remove_quotes)
        return True
