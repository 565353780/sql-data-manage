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

    def reset(self):
        self.title_list = []
        self.title_id_map = {}
        self.data_list_list = []
        self.prompt_list = []
        return True

    def loadTitle(self, title, remove_quotes=False):
        self.title_list = splitLineData(title, remove_quotes)
        for i, title in enumerate(self.title_list):
            self.title_id_map[title] = i
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
                break

        if invalid_data_num > 0:
            print('[WARN][TXTLoader::loadFile]')
            print('\t found', invalid_data_num, 'invalid data!')
        return True

    def generatePrompt(self, query_title_list=None,
                       prompt_type='[TITLE] is [DATA]',
                       prompt_multi_line=False, skip_empty_prompt=False):
        valid_query_title_list = getValidQueryTitleList(
            self.title_list, query_title_list)

        if len(valid_query_title_list) == 0:
            print('[ERROR][TXTLoader::generatePrompt]')
            print('\t valid query title not found!')
            return False

        if '[TITLE]' not in prompt_type or '[DATA]' not in prompt_type:
            print('[ERROR][TXTLoader::generatePrompt]')
            print('\t prompt type not valid!')
            print('\t valid prompt type must contain "[TITLE]" and "[DATA]"!')
            return False

        print('[INFO][TXTLoader::generatePrompt]')
        print('\t start generate prompt for data...')
        for data_list in tqdm(self.data_list_list):
            prompt = getPrompt(self.title_list, self.title_id_map, data_list,
                               valid_query_title_list, prompt_type,
                               prompt_multi_line, skip_empty_prompt)
            self.prompt_list.append(prompt)
        return True
