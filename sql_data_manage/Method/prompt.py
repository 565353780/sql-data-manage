import os
import json
from tqdm import tqdm
from sql_data_manage.Method.path import createFileFolder, removeFile, renameFile


def getUnitPrompt(title, data, prompt_type='[TITLE] is [DATA]',
                  translate_map=None):
    if translate_map is not None and title in translate_map.keys():
        title = translate_map[title]
    return prompt_type.replace('[TITLE]', title).replace('[DATA]', data)


def getPrompt(title_list, title_id_map, data_list, query_title_list,
              prompt_type='[TITLE] is [DATA]',
              multi_line=False, skip_empty=False, translate_map=None):
    assert '[TITLE]' in prompt_type and '[DATA]' in prompt_type

    prompt = ''

    title_num = len(query_title_list)

    iter_idx = 0

    for query_title in query_title_list:
        title_id = title_id_map[query_title]
        title = title_list[title_id]
        data = data_list[title_id]

        iter_idx += 1

        if data == '':
            if skip_empty:
                continue
            else:
                data = 'None'

        prompt += getUnitPrompt(title, data, prompt_type, translate_map)

        if iter_idx == title_num:
            break

        prompt += '\n' if multi_line else ', '
    return prompt


def mergePrompt(prompt_folder_path, dataset_file_path):
    if os.path.exists(dataset_file_path):
        print('[ERROR][prompt::mergePrompt]')
        print('\t dataset file already exist!')
        return False

    if not os.path.exists(prompt_folder_path):
        print('[ERROR][prompt::mergePrompt]')
        print('\t prompt folder not exist!')
        return False

    prompt_json_list = []

    prompt_filename_list = os.listdir(prompt_folder_path)

    print('[INFO][prompt::mergePrompt]')
    print('\t start load all prompts...')
    for prompt_filename in tqdm(prompt_filename_list):
        if prompt_filename[-5:] != '.json':
            continue

        if prompt_filename[-9:] == '_tmp.json':
            continue

        prompt_file_path = prompt_folder_path + prompt_filename
        with open(prompt_file_path, 'r') as f:
            prompt_json = json.load(f)
            prompt_json_list.append(prompt_json)

    createFileFolder(dataset_file_path)
    tmp_dataset_file_path = f'{dataset_file_path[:-5]}_tmp.json'
    removeFile(tmp_dataset_file_path)
    with open(tmp_dataset_file_path, 'w') as f:
        json.dump(prompt_json_list, f, ensure_ascii=False)
    renameFile(tmp_dataset_file_path, dataset_file_path)
    return True
