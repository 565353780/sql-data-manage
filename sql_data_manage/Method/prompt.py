def getUnitPrompt(title, data, prompt_type='[TITLE] is [DATA]'):
    return prompt_type.replace('[TITLE]', title).replace('[DATA]', data)


def getPrompt(title_list, title_id_map, data_list, query_title_list,
              prompt_type='[TITLE] is [DATA]',
              multi_line=False, skip_empty=False):
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

        prompt += getUnitPrompt(title, data, prompt_type)

        if iter_idx == title_num:
            break

        prompt += '\n' if multi_line else ', '
    return prompt
