def getUnitPrompt(title, data, prompt_type='[TITLE] is [DATA]'):
    return prompt_type.replace('A', title).replace('B', data)


def getPrompt(title_list, data_list, prompt_type='[TITLE] is [DATA]',
              multi_line=False, skip_empty=False):
    assert '[TITLE]' in prompt_type and '[DATA]' in prompt_type

    prompt = ''

    title_num = len(title_list)

    iter_idx = 0

    for title, data in zip(title_list, data_list):
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
