import os
from tqdm import tqdm
from sql_data_manage.Module.txt_loader import TXTLoader


class DataMatcher(object):
    def __init__(self, txt_file_path_dict=None, remove_quotes=True):
        self.txt_loader_dict = {}
        self.prompt_list = []
        self.match_data_list_list_list = []

        if txt_file_path_dict is not None:
            self.loadData(txt_file_path_dict, remove_quotes)
        return

    def reset(self):
        if len(self.txt_loader_dict.keys()) > 0:
            for txt_loader in self.txt_loader_dict.values():
                txt_loader.reset()

        self.txt_loader_dict = {}
        self.prompt_list = []
        self.match_data_list_list_list = []
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

    def getUnitMatchDataList(self, match_title):
        title_data_list_list = []

        for key, data_loader in self.txt_loader_dict.items():
            print('[INFO][DataMatcher::getUnitMatchDataList]')
            print('\t start query title [' + match_title + '] in ['
                  + key + ']...')
            success, title_list = data_loader.getData([match_title])
            if not success:
                print('[WARN][DataMatcher::getUnitMatchDataList]')
                print('\t getData for title [' + match_title +
                      '] in [' + key + '] failed!')
                continue

            title_data_list = []
            for row_data in title_list:
                title_data_list.extend(iter(row_data))

            title_data_list = list(set(title_data_list))

            title_data_list_list.append(title_data_list)

        min_size_data_list_idx = -1
        min_size = float('inf')
        for i, title_data_list in enumerate(title_data_list_list):
            current_size = len(title_data_list)
            if current_size < min_size:
                min_size = current_size
                min_size_data_list_idx = i

        assert min_size_data_list_idx != -1

        unit_match_data_set = set(title_data_list_list[min_size_data_list_idx])

        for i, title_data_list in enumerate(title_data_list_list):
            if i == min_size_data_list_idx:
                continue

            unit_match_data_set = unit_match_data_set & set(title_data_list)

        return list(unit_match_data_set)

    def generatePrompt(self, match_title):
        unit_match_data_list = self.getUnitMatchDataList(match_title)
        print('unit_match_data_list:')
        print(len(unit_match_data_list))

        for unit_match_data in tqdm(unit_match_data_list):
            match_data_list_list = []
            for key, data_loader in self.txt_loader_dict.items():
                idx_list = data_loader.getDataIdxList(
                    match_title, unit_match_data)
                if idx_list is None:
                    print('[WARN][DataMatcher::generatePrompt]')
                    print('\t title [' + match_title + '] not found in [' +
                          key + ']!')
                    continue
                success, row_data_list = data_loader.getData(idx_list=idx_list)
                if not success:
                    print('[WARN][DataMatcher::generatePrompt]')
                    print('\t getData for title [' + match_title +
                          '] in [' + key + '] failed!')
                    continue

                match_data_list_list += row_data_list

            self.match_data_list_list_list.append(match_data_list_list)
        return True
