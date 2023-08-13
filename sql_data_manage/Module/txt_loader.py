import os

from sql_data_manage.Method.io import getLineNum, splitLineData
from sql_data_manage.Method.prompt import getPrompt
from sql_data_manage.Method.title import getValidQueryTitleList
from tqdm import tqdm


class TXTLoader(object):
    def __init__(self, txt_file_path=None, remove_quotes=False):
        self.title_list = []
        self.title_id_map = {}
        self.data_list_list = []
        self.prompt_list = []

        if txt_file_path is not None:
            self.loadFile(txt_file_path, remove_quotes)
        return

    @classmethod
    def fromList(cls, data_list):
        cls = TXTLoader()
        cls.title_list = data_list[0]
        cls.data_list_list = data_list[1:]
        cls.generateTitleIDMap()
        return cls

    def reset(self):
        self.title_list = []
        self.title_id_map = {}
        self.data_list_list = []
        self.prompt_list = []
        return True

    def generateTitleIDMap(self):
        for i, title in enumerate(self.title_list):
            self.title_id_map[title] = i
        return True

    def loadTitle(self, title, remove_quotes=False):
        self.title_list = splitLineData(title, remove_quotes)
        self.generateTitleIDMap()
        return True

    def loadFile(self, txt_file_path, remove_quotes=False):
        if not os.path.exists(txt_file_path):
            print('[ERROR][TXTLoader::loadFile]')
            print('\t txt file not exist!')
            print('\t', txt_file_path)

        data_num = getLineNum(txt_file_path) - 1

        invalid_data_num = 0

        print('[INFO][TXTLoader::loadFile]')
        print('\t start load sql txt data...')
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            title = f.readline()

            self.loadTitle(title, remove_quotes)

            for _ in tqdm(range(data_num)):
                data = f.readline()

                if data == '\n':
                    continue

                data_list = splitLineData(data, remove_quotes)

                if len(data_list) != len(self.title_list):
                    invalid_data_num += 1
                    continue

                self.data_list_list.append(data_list)

        if invalid_data_num > 0:
            print('[WARN][TXTLoader::loadFile]')
            print('\t found', invalid_data_num, 'invalid data!')
        return True

    def getRowData(self, idx_list):
        assert idx_list is not None

        if len(idx_list) == 0:
            print('[WARN][TXTLoader::getRowData]')
            print('\t idx_list is empty!')
            return True, []

        row_data = []

        total_data_num = len(self.data_list_list)

        for idx in idx_list:
            if idx < 0 or idx >= total_data_num:
                print('[WARN][TXTLoader::getRowData]')
                print('\t idx [' + str(idx) + '] out of range!')
                continue

            row_data.append(self.data_list_list[idx])

        return True, row_data

    def getColData(self, title_list):
        assert title_list is not None

        if len(title_list) == 0:
            print('[WARN][TXTLoader::getColData]')
            print('\t title_list is empty!')
            return True, []

        title_id_list = []
        for title in title_list:
            if title not in self.title_list:
                print('[WARN][TXTLoader::getColData]')
                print('\t title [' + title + '] not found!')
                continue
            title_id_list.append(self.title_id_map[title])

        total_data_num = len(self.data_list_list)

        col_data = [
            [self.data_list_list[i][title_id] for title_id in title_id_list]
            for i in range(total_data_num)
        ]
        return True, col_data

    def getData(self, title_list=None, idx_list=None):
        if title_list is None:
            if idx_list is None:
                return True, self.data_list_list

            return self.getRowData(idx_list)

        if idx_list is None:
            return self.getColData(title_list)

        title_id_list = []
        for title in title_list:
            if title not in self.title_list:
                print('[WARN][TXTLoader::getData]')
                print('\t title [' + title + '] not found!')
                continue
            title_id_list.append(self.title_id_map[title])

        total_data_num = len(self.data_list_list)

        data = []

        for idx in idx_list:
            if idx < 0 or idx >= total_data_num:
                print('[WARN][TXTLoader::getData]')
                print('\t idx [' + str(idx) + '] out of range!')
                continue

            data.append([self.data_list_list[idx][title_id]
                        for title_id in title_id_list])
        return True, data

    def getDataIdxList(self, title, data):
        if title not in self.title_list:
            print('[ERROR][TXTLoader::getDataIdxList]')
            print('\t title not found!')
            return None

        title_id = self.title_id_map[title]

        idx_list = []

        total_data_num = len(self.data_list_list)

        for i in range(total_data_num):
            current_data = self.data_list_list[i][title_id]
            if current_data == data:
                idx_list.append(i)

        return idx_list

    def generatePrompt(self, query_title_list=None,
                       prompt_type='[TITLE] is [DATA]',
                       prompt_multi_line=False, skip_empty_prompt=False,
                       translate_map=None, print_progress=False):
        valid_query_title_list = getValidQueryTitleList(
            self.title_list, query_title_list)

        if len(valid_query_title_list) == 0:
            print('[ERROR][TXTLoader::generatePrompt]')
            print('\t valid query title not found!')
            return False

        for_data = self.data_list_list
        if print_progress:
            print('[INFO][TXTLoader::generatePrompt]')
            print('\t start generate prompt for data...')
            for_data = tqdm(for_data)
        for data_list in for_data:
            prompt = getPrompt(self.title_list, self.title_id_map, data_list,
                               valid_query_title_list, prompt_type,
                               prompt_multi_line, skip_empty_prompt,
                               translate_map)
            self.prompt_list.append(prompt)
        return True
