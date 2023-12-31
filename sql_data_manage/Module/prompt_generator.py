import json
import os

from sql_data_manage.Config.info_title import INFO_QUERY_TITLE_LIST
from sql_data_manage.Config.info_translate import INFO_EN_CN_MAP
from sql_data_manage.Config.med_title import MED_QUERY_TITLE_LIST
from sql_data_manage.Config.med_translate import MED_EN_CN_MAP
from sql_data_manage.Method.path import createFileFolder, removeFile, renameFile
from sql_data_manage.Method.prompt import mergePrompt
from sql_data_manage.Module.txt_loader import TXTLoader
from tqdm import tqdm


class PromptGenerator(object):
    def __init__(self, dataset_folder_path=None):
        self.file_path_list = []

        if dataset_folder_path is not None:
            self.loadDataset(dataset_folder_path)
        return

    def reset(self):
        self.file_path_list = []
        return True

    def loadDataset(self, dataset_folder_path):
        filename_list = os.listdir(dataset_folder_path)

        for filename in filename_list:
            if filename[-5:] != '.json':
                continue

            if filename[-9:] == '_tmp.json':
                continue

            file_path = dataset_folder_path + filename
            self.file_path_list.append(file_path)
        return True

    def generatePrompt(self, data_file_path, save_file_path):
        if os.path.exists(save_file_path):
            return True

        with open(data_file_path, 'r', encoding='utf-8') as f:
            data_dict = json.load(f)

        med_data_list = data_dict['dat_order_item']
        info_data_list = data_dict['dat_order']

        med_loader = TXTLoader.fromList(med_data_list)
        info_loader = TXTLoader.fromList(info_data_list)

        med_loader.generatePrompt(
            MED_QUERY_TITLE_LIST, '[DATA]',
            skip_empty_prompt=True, translate_map=MED_EN_CN_MAP)
        info_loader.generatePrompt(
            INFO_QUERY_TITLE_LIST, '[DATA]',
            skip_empty_prompt=True, translate_map=INFO_EN_CN_MAP)

        # question_prompt = '患者治疗过程如下:'
        question_prompt = ''
        for prompt in med_loader.prompt_list:
            question_prompt += f'{prompt},'
        # question_prompt += '请问患者的诊断结果是什么?'

        answer_prompt = info_loader.prompt_list[0]

        save_json = {
            'instruction': question_prompt[:-1],
            'input': '',
            'output': answer_prompt,
        }

        createFileFolder(save_file_path)
        tmp_save_file_path = f'{save_file_path[:-5]}_tmp.json'
        removeFile(tmp_save_file_path)
        with open(tmp_save_file_path, 'w', encoding='utf-8') as f:
            json.dump(save_json, f, ensure_ascii=False)
        renameFile(tmp_save_file_path, save_file_path)
        return True

    def generateAllPrompt(self, save_folder_path, dataset_file_path):
        print('[INFO][PromptGenerator::generateAllPrompt]')
        print('\t start generate prompt dataset...')
        for file_path in tqdm(self.file_path_list):
            file_basename = file_path.split('/')[-1].split('.')[0]
            save_file_path = save_folder_path + file_basename + '.json'
            self.generatePrompt(file_path, save_file_path)
        return True

    def generatePromptDataset(self, save_folder_path, dataset_file_path,
                              train_percent):
        return mergePrompt(save_folder_path, dataset_file_path, train_percent)
